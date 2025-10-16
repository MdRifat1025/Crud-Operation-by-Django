from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomerUserCreationForm(UserCreationForm):
    class meta:
        models=CustomUser
        fields=[
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]