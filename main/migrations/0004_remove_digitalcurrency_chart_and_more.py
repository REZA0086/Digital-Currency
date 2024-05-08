# Generated by Django 5.0.1 on 2024-04-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_digitalcurrency_symbol_delete_currencygallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalcurrency',
            name='chart',
        ),
        migrations.RemoveField(
            model_name='digitalcurrency',
            name='circulating_supply',
        ),
        migrations.RemoveField(
            model_name='digitalcurrency',
            name='market_cap',
        ),
        migrations.RemoveField(
            model_name='digitalcurrency',
            name='total_supply',
        ),
        migrations.RemoveField(
            model_name='digitalcurrency',
            name='volume_24h',
        ),
        migrations.AddField(
            model_name='digitalcurrency',
            name='currency',
            field=models.CharField(max_length=250, null=True, verbose_name='واحد پول'),
        ),
        migrations.AddField(
            model_name='digitalcurrency',
            name='full_name',
            field=models.CharField(max_length=100, null=True, verbose_name='نام کامل ارز دیجیتال'),
        ),
        migrations.AlterField(
            model_name='digitalcurrency',
            name='current_price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True, verbose_name='قیمت فعلی ارز'),
        ),
    ]
