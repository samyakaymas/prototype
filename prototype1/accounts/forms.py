from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CK
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm

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

class CKForm(ModelForm):
    # content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = CK
        fields = "__all__"