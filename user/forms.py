from django import forms
from .models import *




class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
    