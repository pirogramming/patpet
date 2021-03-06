from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='', required=False, widget=forms.FileInput(attrs={
        'class': 'post-new-photo',
    }))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자 까지 등록 가능합니다.\n#태그명을 통해서 검색 태그를 등록할 수 있습니다. \n예시 : #like #patpet!', }))

    class Meta:
        model = Post
        fields = ['photo', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'comment-form',
        'size': '63px',
        'placeholder': '댓글 달기...',
        'maxlength': '40', }))

    class Meta:
        model = Comment
        fields = ['content']