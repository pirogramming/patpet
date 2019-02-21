from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from allauth.socialaccount.forms import SignupForm

from .models import Profile, Archive, Message


class CustomSocialSignupForm(SignupForm):
    # phone_number = forms.CharField()
    # address = forms.CharField()
    email = forms.EmailField(required=True, label='Email')
    # class Meta(SignupForm.Meta):
    #     fields = SignupForm.Meta.fields + ('email',)

    def save(self, request):
        user = super(CustomSocialSignupForm, self).save(request)
        profile = Profile.objects.create(
            user = user,
            # phone_number= self.cleaned_data['phone_number'],
            # address = self.cleaned_data['address'],

        )
        return user


class SignupForm(UserCreationForm):
    # phone_number = forms.CharField()
    # address = forms.CharField()
    email = forms.EmailField(required=True, label='Email')
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            # phone_number= self.cleaned_data['phone_number'],
            # address = self.cleaned_data['address'],

        )
        return user

class ProfileForm(forms.ModelForm):
    pic = forms.ImageField(label='', required=False, widget=forms.FileInput(attrs={
        'class': 'profile-photo',
    }))
    introduce = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'profile-introduce',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자 까지 등록 가능합니다.\n나를 소개하세요', }))
    class Meta:
        model = Profile
        fields = ['pic', 'introduce']

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = ['archive']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'message']

class MessageForm2(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']