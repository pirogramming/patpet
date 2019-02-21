from django import forms
from .models import CommunicationPost, CommunicationComment


class PostForm(forms.ModelForm):
    class Meta:
        model = CommunicationPost
        fields = ['title', 'content', 'photo']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'comment-form',
        'size': '63px',
        'placeholder': '댓글 달기...',
        'maxlength': '40', }))

    class Meta:
        model = CommunicationComment
        fields = ['content']