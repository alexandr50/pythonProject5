from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserRegisterForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('phone_number',)


class ConfirmCodeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('verify_code',)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
