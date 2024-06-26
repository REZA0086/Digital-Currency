# Generated by Django 5.0.1 on 2024-05-12 13:36

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان خبر')),
                ('content', models.TextField(verbose_name='متن خبر')),
                ('created_time', django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ساخت خبر')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده خبر')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'اخبار',
            },
        ),
    ]
