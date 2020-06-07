from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=254, required=True)
    chapter = forms.CharField(max_length=30, required=True)
    subject = forms.CharField(max_length=30, required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'chapter', 'subject')

class SignInForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')