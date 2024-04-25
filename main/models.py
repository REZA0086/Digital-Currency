from django.db import models
from django_jalali.db import models as jmodels


class DigitalCurrency(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام ارز دیجیتال")
    symbol = models.CharField(max_length=10, verbose_name="نماد ارز دیجیتال")
    current_price = models.DecimalField(max_digits=20, decimal_places=10, verbose_name="قیمت فعلی ارز")
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="سرمایه بازار ارز")
    volume_24h = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حجم معاملات 24 ساعت اخیر")
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="مقدار فعلی ارز در گردش")
    total_supply = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="مقدار کل ارز")
    chart = models.IntegerField(verbose_name="نمودار")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ارز دیجیتال"
        verbose_name_plural = "ارز های دیجیتال"


class CurrencyGallery(models.Model):
    image = models.ImageField(upload_to='media/gallery/', verbose_name="عکس")
    currency = models.ForeignKey(DigitalCurrency, on_delete=models.CASCADE, verbose_name="ارز دیجیتال")
