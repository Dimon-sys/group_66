from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'password1', 'password2']
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    
            
