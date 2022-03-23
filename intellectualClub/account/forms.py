from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# REGISTER FORM START


class RegisterUserForm (UserCreationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# REGISTER FORM END

# LOGIN FORM START


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# LOGIN FORM END
