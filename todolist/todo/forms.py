from django import forms
from .models import Todo, Item


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
