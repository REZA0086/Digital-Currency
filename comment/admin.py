from django.contrib import admin
from comment.models import *

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')
