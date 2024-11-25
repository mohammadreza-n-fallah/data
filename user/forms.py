from django import forms
from .models import *




class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        labels = {
            'username': "",
            'password': "",

        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'width: 200px;border-radius: 8px;height:40px;border: 4px solid white ;padding: 5px;',
                'placeholder': 'نام کاربری...'
            }),
            'password': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'width: 200px;border-radius: 8px;height:40px;border: 4px solid white ;padding: 5px;',
                'placeholder': 'رمز...'
            }),

        }
    