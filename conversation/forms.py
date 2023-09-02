from django import forms

from .models import ItemMessage

# class UserMessageForm(forms.ModelForm):
#     content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}))

#     class Meta:
#         model = ItemMessage 
#         fields = ('content',)

class ItemMessageForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl border'}))

    class Meta:
        model = ItemMessage 
        fields = ('content',)