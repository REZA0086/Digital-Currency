from django.contrib import admin
from main.models import *

@admin.register(DigitalCurrency)
class DigitalCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name','current_price')



