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
    image = forms.ImageField(required=False, label='Imagem da Box')  # Campo para upload de imagem

    class Meta:
        model = Box
        fields = ('name', 'tag', 'price', 'description', 'image')
        labels = {
            'name': 'Nome da Box',
            'tag': 'Tag da Box',
            'price': 'Preço',
            'description': 'Descrição sobre a Box',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da Box'}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escolha uma tag para a Box'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva a descrição aqui'}),
        }

# Esse abaixo NÃO está sendo usado
class BoxFormUpdate(forms.ModelForm):
    image = forms.ImageField(required=False, label='Imagem da Box')  # campo para upload de imagem

    class Meta: 
        model = Box
        fields = ('name', 
                  'tag', 
                  'seller', 
                  'price',
                  'description' )
        labels = {
            'name': 'Nome da Box',
            'tag': 'Tag da Box',
            'seller': 'Vendedor',
            'price': 'Preço',
            'description': 'Descrição sobre a Box',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'seller': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorID', 'type': 'hidden'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Escreva a descrição aqui'})
        }