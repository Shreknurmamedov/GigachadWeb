from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'year']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'

            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Faceit level'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),

            "year": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            })



        }
