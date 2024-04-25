from django.contrib import admin
from news.models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')