from .models import Sushi
from django.forms import ModelForm, TextInput, Textarea


class SushiForm(ModelForm):
    class Meta:
        model = Sushi
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввидите название'
                }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ввидите описание'
                }),
        }