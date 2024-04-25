# Generated by Django 5.0.1 on 2024-04-24 15:58

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام ارز دیجیتال')),
                ('symbol', models.CharField(max_length=10, verbose_name='نماد ارز دیجیتال')),
                ('current_price', models.DecimalField(decimal_places=10, max_digits=20, verbose_name='قیمت فعلی ارز')),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='سرمایه بازار ارز')),
                ('volume_24h', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='حجم معاملات 24 ساعت اخیر')),
                ('circulating_supply', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='مقدار فعلی ارز در گردش')),
                ('total_supply', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='مقدار کل ارز')),
            ],
            options={
                'verbose_name': 'ارز دیجیتال',
                'verbose_name_plural': 'ارز های دیجیتال',
            },
        ),
        migrations.CreateModel(
            name='CryptocurrencyPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=10, max_digits=20, verbose_name='قیمت ارز دیجیتال در زمان مشخص')),
                ('timestamp', django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ثبت قیمت')),
                ('cryptocurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.digitalcurrency', verbose_name='ارز دیجیتال')),
            ],
            options={
                'verbose_name': 'محاسبه قیمت ارز',
                'verbose_name_plural': 'محاسبات قیمت ارز',
            },
        ),
    ]