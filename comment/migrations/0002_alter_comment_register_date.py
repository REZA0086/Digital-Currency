# Generated by Django 5.0.1 on 2024-04-25 09:10

import datetime
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='register_date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2024, 4, 25), verbose_name='تاریخ درج'),
        ),
    ]
