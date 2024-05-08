from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'type':"text",'class':"form-control mini-form__input", 'placeholder':"نظر خود را درمورد سایت ما بیان کنید"})
        }