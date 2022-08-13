from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        fields=[
            'username', 
            'email', 
            'password1', 
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        
        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Username','autofocus':None})
        self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder': 'E-mail'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'})