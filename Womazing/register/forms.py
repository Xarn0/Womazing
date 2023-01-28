from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class UserForm(UserCreationForm):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'ob_input forms_reg_input', 'placeholder' : 'Логин'}))
    email = forms.CharField(label = '', widget= forms.EmailInput(attrs={'class': 'ob_input forms_reg_input','placeholder' : 'Email'}))
    password1 =  forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'ob_input forms_reg_input','placeholder' : 'Пароль'}))
    password2 =  forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'ob_input forms_reg_input','placeholder' : 'Подтвердите пароль'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
