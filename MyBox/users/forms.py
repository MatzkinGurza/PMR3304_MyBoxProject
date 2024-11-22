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
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'First name'}))
    last_name = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'First name'}))
    last_name = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))
    username = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password', 'username')


class UserProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        choices=[("buyer", "Buyer"), ("seller", "Seller")], 
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    
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
        def clean(self):
            cleaned_data = super().clean()
            user = self.instance.user

            # Check if the user already has a profile
            if Profile.objects.filter(user=user).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("This user already has a profile.")
            
            return cleaned_data


class StoreForm(forms.ModelForm):
    logo = forms.ImageField(required=False)
    background = forms.ImageField(required=False)

    class Meta:
        model = Store
        fields = ('store_name', 'store_email', 'cnpj', 'store_description')
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'store name'}), 
            'store_email': forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'cnpj'}), 
            'store_description': forms.Textarea(attrs={'class': 'form-control','placeholder':'description'}),
        }