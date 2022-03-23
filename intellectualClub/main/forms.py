
from dataclasses import field
from unicodedata import name
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

# АDD EVENT FORM START


class AddEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Event
        fields = ['title', 'slug', 'description',
                  'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cat': forms.Select(attrs={'class': 'form-select'}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

# АDD EVENT FORM END

# ORDER FORM START


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

# ORDER FORM END

# ACCOUNT USER SETTINGS FORM START


class UserSettingsForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'first_name']
# ACCOUNT USER SETTINGS FORM END
