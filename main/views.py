import requests
from django.conf import settings
from django.http import JsonResponse
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from analysis.models import Analysis
from comment.models import Comment
from main.models import DigitalCurrency
from comment.forms import CommentForm
from news.models import News


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

    return {'currency': data5, 'currency_list': data1, 'currency_name': data2, 'currency_price': data3, 'data4': data4}


class IndexView(View):
    def get(self, request):
        context = {}
        currency_change_request = request.GET.get('currency')

        get_currency_data = get_currency(request)
        currency_list = get_currency_data['currency']
        for key, value in currency_list.items():
            DigitalCurrency.objects.create(name=key, current_price=value)
        digital_currency = DigitalCurrency.objects.all()[:10]

        for key, value in currency_list.items():
            if key == "BTC":
                btc_price = value

        for key, value in currency_list.items():
            if key == str(currency_change_request):
                context['price'] = value
                print(context['price'])
        form = CommentForm()
        comments = Comment.objects.filter(is_active=True).order_by('-register_date')
        analysis = Analysis.objects.all().order_by('-created_time')
        news = News.objects.all().order_by('created_time')

        context['media_url'] = settings.MEDIA_URL
        context['digital_currency'] = digital_currency
        context['form'] = form
        context['comments'] = comments
        context['analysis'] = analysis
        context['news'] = news
        return render(request, 'index.html', context)
