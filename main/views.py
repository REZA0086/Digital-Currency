import requests
from django.conf import settings
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from analysis.models import Analysis
from comment.models import Comment
from main.models import DigitalCurrency
from comment.forms import CommentForm
from news.models import News
from django.db import transaction
from main.forms import CurrencyForm


def media_admin(request):
    return {'media_url': settings.MEDIA_URL, }


def get_currency(request):
    url = 'https://api.kucoin.com/api/v3/currencies'
    response = requests.get(url)
    data = response.json()
    for key, value in data.items():
        if key != 'code':
            data1 = [key, value]

    data2 = []
    for key in data1[1]:
        data2.append(key)

    data3 = []
    for item in data2:
        for x, y in item.items():
            if x == 'currency':
                data3.append(y)

    url_price = 'https://api.kucoin.com/api/v1/prices'
    response_price = requests.get(url_price)
    data_price = response_price.json()
    for key, value in data_price.items():
        data_price1 = [value]

    data4 = {}
    for item in data_price1:
        for x, y in item.items():
            data4[x] = y

    data5 = {}
    for name in data3:
        for v, k in data4.items():
            if v == name:
                data5[name] = k
    all_market = {}
    substring_to_remove = "-USDT"
    url_market = 'https://api.kucoin.com/api/v1/market/allTickers'
    response_market_all = requests.get(url_market)
    response_market = response_market_all.json()

    chang = response_market['data']['ticker']
    for item in chang:
        for name in data3:
            if item['symbol'].replace(substring_to_remove, "") == name:
                all_market[name] = item['changePrice']

    url_chart = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=2"
    response_chart = requests.get(url_chart)
    data = response_chart.json()
    list_chart = []
    for key, value in data.items():
        for val in value:
            list_chart.append(val[1])

    return {'currency': data5,'all_market': all_market, 'chart': list_chart}


class IndexView(View):
    def get(self, request):

        context = {}
        final_price = request.session.get('final_price')
        context['final_price'] = final_price
        get_currency_data = get_currency(request)
        currency_list = get_currency_data['currency']
        all_market = get_currency_data['all_market']
        chart = get_currency_data['chart']
        print(chart)
        for currency_name, currency_price in currency_list.items():
            if currency_name in all_market:
                DigitalCurrency.objects.create(name=currency_name, current_price=currency_price,
                                               changePrice=all_market[currency_name])

        digital_currency = DigitalCurrency.objects.all()[:10]
        form = CommentForm()
        comments = Comment.objects.filter(is_active=True).order_by('-register_date')
        analysis = Analysis.objects.all().order_by('-created_time')
        news = News.objects.all().order_by('created_time')

        form_currency = CurrencyForm()
        context['media_url'] = settings.MEDIA_URL
        context['digital_currency'] = digital_currency
        context['form'] = form
        context['comments'] = comments
        context['analysis'] = analysis
        context['news'] = news
        context['form_currency'] = form_currency
        context['chart'] = chart

        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        currency_change_request = request.POST.get('currency')
        print(currency_change_request)
        get_currency_data = get_currency(request)
        currency_list = get_currency_data['currency']

        count = request.POST.get('count')
        for key, value in currency_list.items():
            if key == str(currency_change_request):
                final_price = int(count) / float(value)
                request.session['final_price'] = final_price
                return JsonResponse({'final_price': final_price})
        return JsonResponse({'final_price': None})
