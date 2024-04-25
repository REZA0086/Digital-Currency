from django.db import models
from django_jalali.db import models as jmodels
from django.db import models
from account.models import CustomerUser


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان خبر")
    author = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name="نویسنده خبر")
    content = jmodels.jDateField(auto_now=True, verbose_name="تاریخ ساخت خبر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
