from django.db import models
from django_jalali.db import models as jmodels
from account.models import CustomerUser
from main.models import *


class Analysis(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان تحلیل")
    description = models.TextField(verbose_name="متن تحلیل")
    created_time = jmodels.jDateField(auto_now=True, verbose_name="تاریخ ثبت")
    user = models.ForeignKey(CustomerUser, verbose_name="کاربر", on_delete=models.CASCADE)
    currency = models.ForeignKey(DigitalCurrency, on_delete=models.CASCADE, verbose_name="ارز دیجیتال")

    class Meta:
        verbose_name = "تحلیل"
        verbose_name_plural = "تحلیل ها"


