from django import forms
from myblog.models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author","category", "body")

        widgets = {
            'category': forms.Select(choices=choice_list),
            "author": forms.TextInput(attrs={'id': 'author', 'value': '', 'type': 'hidden'})

        }
