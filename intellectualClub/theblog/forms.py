from .models import Post
from django import forms


class PostForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название записи'}),
            'author': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Выберите автора'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержимое записи'})
        }
