# Generated by Django 5.0.1 on 2024-05-01 15:10

import datetime
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_alter_comment_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='register_date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2024, 5, 1), verbose_name='تاریخ درج'),
        ),
    ]
