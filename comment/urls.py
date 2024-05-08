from django.urls import path
from comment import views

app_name = 'comment'
urlpatterns = [
    path('', views.CommentView.as_view(), name='comment')
]