from django import forms
from .models import Profile, Store
from django.contrib.auth.models import User
import requests
from typing import Any
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Primeiro nome'}), label='Primeiro nome')
    last_name = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Último nome'}), label='Último nome')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}), label='Email')
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Primeiro nome'}), label='Primeiro nome')
    last_name = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Último nome'}), label='Último nome')
    username = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Usuário'}), label='Usuário')
    
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        choices=[("buyer", "Comprador"), ("seller", "Vendedor")], 
        widget=forms.Select(attrs={'class': 'form-control'})
        , label = 'Tipo de usuário')
    
    class Meta:
        model = Profile
        fields = ('phone', 'cpf', 'birth_date', 'address', 'complement', 'cep')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':''}), 
            'cpf': forms.TextInput(attrs={'class': 'form-control','placeholder':''}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'birth date'}), 
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'address'}),
            'complement': forms.TextInput(attrs={'class': 'form-control','placeholder':''}),
            'cep': forms.NumberInput(attrs={'class': 'form-control','placeholder':''}),
        }
        labels = {
            'phone': 'Telefone',
            'cpf': 'CPF',
            'birth_date': 'Data de nascimento',
            'address': 'Endereço',
            'complement': 'Complemento',
            'cep': 'CEP',
        }
        def clean(self):
            cleaned_data = super().clean()
            user = self.instance.user

            # Check if the user already has a profile
            if Profile.objects.filter(user=user).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Esse usuário já possui um perfil.")
            
            return cleaned_data
    def clean_user_type(self):
        user_type = self.cleaned_data.get('user_type')
        if user_type not in ["buyer", "seller"]:
            raise forms.ValidationError("Selecione um tipo de usuário válido.")
        return user_type


class StoreForm(forms.ModelForm):
    logo = forms.ImageField(required=False)
    background = forms.ImageField(required=False, label='Imagem de fundo')

    class Meta:
        model = Store
        fields = ('store_name', 'store_email', 'cnpj', 'store_description')
        labels = {
            'store_name': 'Nome da loja',
            'store_email': 'E-mail da loja',
            'cnpj': 'CNPJ',
            'store_description': 'Descrição da loja',
        }
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nome da loja'}), 
            'store_email': forms.TextInput(attrs={'class': 'form-control','placeholder':'E-mail'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'CNPJ'}), 
            'store_description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Descrição da loja'}),
        }