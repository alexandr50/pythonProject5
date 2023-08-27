from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserRegisterForm(forms.Form):

    phone_number = forms.CharField(max_length=13)


class ConfirmCodeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('verify_code',)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('phone_number', )
