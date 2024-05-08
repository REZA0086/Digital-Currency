from django.shortcuts import render, redirect
from django.views.generic import View
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib import messages


# Create your views here.
class CommentView(View):
    def get(self, request):
        return redirect('main:index')

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(user=request.user, comment=form.cleaned_data['comment'], is_active=False)
            messages.success(request, 'نظر شما با موفقیت ثبت شد منتظر تایید ادمین باشید')
            return redirect('main:index')
        else:
            messages.error(request, 'اطلاعات معتبر نمی باشد')
        return redirect('main:index')
