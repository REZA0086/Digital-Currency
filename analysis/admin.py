from django.contrib import admin
from analysis.models import *


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
