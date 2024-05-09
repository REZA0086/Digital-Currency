from django import forms

from account.models import CustomerUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['user_phone', 'password', 'active_code']
        widgets = {
            'user_phone': forms.TextInput(attrs={'type': "text", 'class': "form-control", 'maxlength': '11',
                                                 'placeholder': "شماره تلفن خود را وارد کنید"}),
            'password': forms.TextInput(
                attrs={'type': "password", 'class': "form-control", 'placeholder': "پسورد خود را وارد کنید"}),
            'active_code': forms.TextInput(attrs={'type': "text", 'class': "form-control",
                                                  'placeholder': "کد ارسال شده به تلفن خود را وارد کنید"}),
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['user_phone', 'name', 'family', 'password']
        widgets = {
            'user_phone': forms.TextInput(attrs={'type': "text", 'class': "form-control", 'maxlength': '11',
                                                 'placeholder': "شماره تلفن خود را وارد کنید"}),
            'name': forms.TextInput(
                attrs={'type': "text", 'class': "form-control", 'placeholder': "نام خود را وارد کنید"}),
            'family': forms.TextInput(attrs={'type': "text", 'class': "form-control",
                                             'placeholder': "نام خانوادگی خود را وارد کنید"}),
            'password': forms.TextInput(attrs={'type': "password", 'class': "form-control",
                                               'placeholder': "پسورد خود را وارد کنید"}),
        }


class RecoveryPassForm(forms.Form):
    user_phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control", 'maxlength': '11', 'placeholder': "شماره تلفن خود را وارد کنید"
    }))


class ActiveCodeForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['active_code']
        widgets = {
            'active_code': forms.TextInput(attrs={'type': "text", 'class': "form-control", 'maxlength': '6',
                                                  'placeholder': "کد ارسال شده به تلفن خود را وارد کنید"})
        }


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['password']
        widgets = {
            'password': forms.TextInput(attrs={'type': "text", 'class': "form-control",
                                               'placeholder': "پسورد جدید خود را وارد کنید"})
        }
