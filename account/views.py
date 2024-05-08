from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
import requests
from account.forms import *
import random


def generate_random_number():
    random_number = random.randint(100000, 999999)
    random_number_str = str(random_number).zfill(6)
    return random_number_str


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        opt_code = generate_random_number()
        print(opt_code)
        request.session['opt_code'] = opt_code
        return render(request, 'account/login.html', {'form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        user_phone = login_form.data['user_phone']
        code = login_form.data['active_code']
        opt_code = request.session.get('opt_code')

        try:
            user = CustomerUser.objects.get(user_phone=user_phone)

            data = {'bodyId': 0000, 'to': f'{user_phone}', 'args': [str(opt_code)]}
            response = requests.post('http://127.0.0.1:8000', json=data)
            if code == opt_code:
                if user.check_password(login_form.data['password']):
                    user.is_active = True
                    login(request, user)
                    messages.success(request, 'با موفقیت وارد شدید.')
                    return redirect('main:index')
                else:
                    messages.error(request, 'کلمه عبور اشتباه است.')
            else:
                messages.error(request, 'کد وارد شده صحیح نمی باشد')
        except CustomerUser.DoesNotExist:
            messages.error(request, 'کاربر مورد نظر با این شماره تلفن یافت نشد')

        context = {'form': login_form}
        return render(request, 'account/login.html', context)


class RegisterView(View):
    template_name = 'account/register.html'

    def get(self, request):
        register_form = RegisterForm()
        context = {
            'form': register_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_phone = register_form.cleaned_data['user_phone']
            password = register_form.cleaned_data['password']
            name = register_form.cleaned_data['name']
            family = register_form.cleaned_data['family']
            user = CustomerUser.objects.filter(user_phone=user_phone).exists()
            if user:
                messages.error(request, 'شماره موبایل شما تکراری می باشد')
            else:
                CustomerUser.objects.create_user(
                    user_phone=user_phone,
                    name=name,
                    family=family,
                    password=password
                )
                messages.success(request, 'ثبت نام با موفقیت انجام شد')
                return redirect('account:login')
        else:
            messages.error(request, 'فرم شما نامعتبر است')
        context = {
            'form': register_form
        }
        return render(request, self.template_name, context)
