from django.db import models

from account.models import CustomerUser
from django_jalali.db import models as jmodels
import jdatetime


class Comment(models.Model):
    comment = models.TextField(verbose_name='نظر')
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ درج')
    is_active = models.BooleanField(default=False, verbose_name='تایید / عدم تایید')
    user = models.ForeignKey(CustomerUser, on_delete=models.PROTECT, related_name='user_comment', verbose_name='کاربر ')

    class Meta:
        verbose_name = 'نظرات '
        verbose_name_plural = 'نظرات '

    def __str__(self):
        return f'{self.user} - {self.comment}'