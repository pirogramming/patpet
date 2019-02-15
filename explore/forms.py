from django import forms
from .models import CommunicationPost, CommunicationComment


class PostForm(forms.ModelForm):
    class Meta:
        model = CommunicationPost
        fields = '__all__'


class CommentForm(forms.ModelForm):
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요!', 'rows': '4', 'cols': '50'}))
    class Meta:
        model = CommunicationComment
        fields = ['message']
