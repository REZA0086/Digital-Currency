from django.db import models
from django_jalali.db import models as jmodels


class DigitalCurrency(models.Model):
    currency = models.CharField(max_length=250,verbose_name="واحد پول",null=True,blank=True)
    name = models.CharField(max_length=100, verbose_name="نام ارز دیجیتال")
    full_name = models.CharField(max_length=100, verbose_name="نام کامل ارز دیجیتال",null=True,blank=True)
    symbol = models.ImageField(upload_to='media/symbol/', verbose_name="نماد ارز دیجیتال",null=True, blank=True)
    current_price = models.DecimalField(max_digits=20, decimal_places=10, verbose_name="قیمت فعلی ارز",null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ارز دیجیتال"
        verbose_name_plural = "ارز های دیجیتال"



