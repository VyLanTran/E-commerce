from django import forms
from .models import Item 

INPUT_CLASSES = 'w-full p-2 border border-gray-700 rounded-md'


class AddItemForm(forms.ModelForm):
    
    class Meta: 
        model = Item
        fields = ( 'name', 'category','description', 'price','is_new', 'image', 'quantity')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class':  'w-[200px] p-2 border border-gray-700 rounded-md'
            }),
            'image': forms.FileInput(attrs={
                'class': ''
            }),
            'quantity': forms.TextInput(attrs={
                'class': 'w-[200px] p-2 border border-gray-700 rounded-md'
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category','description', 'price','is_new', 'image', 'quantity')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class':  'w-[200px] p-2 border border-gray-700 rounded-md'
            }),
            'image': forms.FileInput(attrs={
                'class': ''
            }),
            'quantity': forms.TextInput(attrs={
                'class': 'w-[200px] p-2 border border-gray-700 rounded-md'
            }),
        }