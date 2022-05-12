from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

# REGISTER FORM START


# class RegisterUserForm (UserCreationForm):
#     username = forms.CharField(
#         label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(
#         label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(
#         label='Ваша фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(
#         label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(
#         label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(
#         attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email',
#                   'password1', 'password2')

# REGISTER FORM END

# LOGIN FORM START


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# LOGIN FORM END

# EDIT USER PROFILE FORM START


class EditUserForm(UserChangeForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


# EDIT USER PROFILE FORM END

# CHANGE PASSWORD FORM START

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Введите старый пароль:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(label='Введите новый пароль:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label='Повторите новый пароль:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2', )

# CHANGE PASSWORD FORM END
