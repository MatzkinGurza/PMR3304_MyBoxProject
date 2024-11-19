from django import forms
from .models import Box

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['name', 'tag', 'price', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
