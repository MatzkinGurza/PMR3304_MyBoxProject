from django import forms
from .models import Box

# class BoxForm(forms.ModelForm):
#     class Meta:
#         model = Box
#         fields = ['name', 'tag', 'price', 'description', 'image']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }

class BoxForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # campo para upload de imagem

    class Meta: 
        model = Box
        fields = ('name', 
                  'tag', 
                  'seller', 
                  'price',
                  'description' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'seller': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorID', 'type': 'hidden'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'write your post here'})
        }

class BoxFormUpdate(forms.ModelForm):
    image = forms.ImageField(required=False)  # campo para upload de imagem

    class Meta: 
        model = Box
        fields = ('name', 
                  'tag', 
                  'seller', 
                  'price',
                  'description' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'seller': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorID', 'type': 'hidden'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'write your post here'})
        }