from django import forms


class CurrencyForm(forms.Form):
    form_count = forms.IntegerField()
    widgets = {
        'form_count': forms.TextInput(attrs={'type': "number", 'class': "form-control forms-purchase__value"}),
    }
