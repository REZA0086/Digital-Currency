# Generated by Django 5.0.1 on 2024-04-24 15:54

import datetime
import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_phone', models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('family', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='عکس پروفایل کاربری')),
                ('register_date', django_jalali.db.models.jDateField(default=datetime.date(2024, 4, 24), verbose_name='تاریخ ثبت نام')),
                ('active_code', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت کاربر')),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='SellerUser',
            fields=[
                ('customeruser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.customeruser',),
        ),
    ]
