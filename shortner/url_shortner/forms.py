from django import forms

from .models import Web_URL

class ShirinkForm(forms.ModelForm):
    class Meta:
        model = Web_URL
        fields = ('url',)
        widgets={
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control input-lg chat-input',
                    'placeholder': 'http://example.org'
                }
            )
        }
