from django import forms
from .models import CommunicationPost, CommunicationComment


class PostForm(forms.ModelForm):
    class Meta:
        model = CommunicationPost
        fields = ['title', 'content', 'photo']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'comment-form',
        'size': '40px',
        'placeholder': '내용을 입력하세요.',
        'rows': '4',
        'cols': '50',}))

    class Meta:
        model = CommunicationComment
        fields = ['author', 'content']
