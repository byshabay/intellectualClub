from theblog.models import Post, Category
from django import forms

choises = Category.objects.all().values_list('name', 'name')

choise_list = []

for item in choises:
    choise_list.append(item)


class PostForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название записи'}),
            'author': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Выберите автора'}),
            'category':  forms.Select(choices=choise_list, attrs={'class': 'form-select', 'placeholder': 'Выберите категорию'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержимое записи'}),
        }
