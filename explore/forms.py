from django import forms
from .models import CommunicationPost, CommunicationComment


class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='', required=False)
    title = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 2,
        'cols': 50,
        'placeholder': '제목을 적어주세요.', }))

    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '내용을 적어주세요. ', }))

    class Meta:
        model = CommunicationPost
        fields = ['title', 'content', 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommunicationComment
        fields = ['content']
