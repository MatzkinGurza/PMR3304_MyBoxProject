from django import forms
from .models import Profile, Store, Subscription, Payment
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
    tipo_de_usuário = forms.ChoiceField(
        choices=[("buyer", "Comprador"), ("seller", "Vendedor")], 
        widget=forms.Select(attrs={'class': 'form-control'})
        , label = 'Tipo de usuário')
    
    class Meta:
        model = Profile
        fields = ('telefone', 'CPF', 'nascimento', 'endereço', 'complemento', 'CEP', 'tipo_de_usuário')
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control','placeholder':''}), 
            'CPF': forms.TextInput(attrs={'class': 'form-control','placeholder':''}),
            'nascimento': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'birth date'}, 
                format='%d/%m/%Y'),
            'endereço': forms.TextInput(attrs={'class': 'form-control','placeholder':'address'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control','placeholder':''}),
            'CEP': forms.NumberInput(attrs={'class': 'form-control','placeholder':''}),
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

class EditStoreForm(forms.ModelForm):
    logo = forms.ImageField(required=False, label='Logo da loja', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
   
    class Meta:
        model = Store
        fields = ('store_name', 'store_email', 'cnpj', 'store_description', 'logo')
        labels = {
            'store_name': 'Nome da loja',
            'store_email': 'E-mail da loja',
            'cnpj': 'CNPJ',
            'store_description': 'Descrição da loja',
            'logo': 'Logo da loja',
        }
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da loja'}),
            'store_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail da loja'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ'}),
            'store_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da loja'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
           
#class SubscriptionForm(forms.ModelForm):
 #   class Meta:
   #     model = Subscription
  #      fields = ['store']

from django import forms
from .models import Payment
from datetime import datetime

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['nome_no_cartão', 'número_do_cartão', 'validade', 'CPF_do_titular', 'PIN']
        widgets = {
            'nome_no_cartão': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nome no cartão'
            }),
            'número_do_cartão': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Número do cartão'
            }),
            'validade': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'DD/MM/AA', 
                'type': 'text'
            }),
            'CPF_do_titular': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'CPF do titular'
            }),
            'PIN': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': 'PIN'
            }),
        }
        labels = {
            'nome_no_cartão': 'Nome no cartão',
            'número_do_cartão': 'Número do cartão',
            'validade': 'Validade (DD/MM/AA)',
            'CPF_do_titular': 'CPF do titular',
            'PIN': 'PIN',
        }
