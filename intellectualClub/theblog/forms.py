from theblog.models import Post, Category
from django import forms

choises = Category.objects.all().values_list('name', 'name')

choise_list = []

for item in choises:
    choise_list.append(item)


class PostForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'header_image',
                  'author', 'category', 'body', 'snippet']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название записи'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'post_author', 'type': 'hidden'}),
            'category':  forms.Select(choices=choise_list, attrs={'class': 'form-select', 'placeholder': 'Выберите категорию'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержимое записи'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите краткое содержимое записи'}),
        }
