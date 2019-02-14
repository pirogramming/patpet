from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from allauth.socialaccount.forms import SignupForm

from .models import Profile


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
