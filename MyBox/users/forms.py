from django import forms
from .models import Profile, Store
from django.contrib.auth.models import User
import requests


class UserProfileForm(forms.ModelForm):
    # Campos adicionais do usuário
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Profile
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name',
            'phone', 'cpf', 'birth_date', 'address', 'complement', 'cep', 'user_type'
        ]

    def save(self, commit=True):
        # Criação do usuário associado ao perfil
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )

        # Evitar criar perfis duplicados
        if Profile.objects.filter(user=user).exists():
            raise ValueError("Um perfil já existe para este usuário.")

        profile = super().save(commit=False)
        profile.user = user

        if commit:
            user.save()
            profile.save()

        return profile
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        cpf = cleaned_data.get('cpf')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")

        if Profile.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está em uso.")

        return cleaned_data


class StoreForm(forms.ModelForm):
    logo = forms.ImageField(required=False)
    background_image = forms.ImageField(required=False)

    class Meta:
        model = Store
        fields = ['store_name', 'store_email', 'cnpj', 'logo', 'background_image', 'store_description']

    def save(self, commit=True):
        store = super().save(commit=False)

        if 'logo' in self.files and self.files['logo']:
            store.logo = self.upload_to_imgur(self.files['logo'])
        if 'background_image' in self.files and self.files['background_image']:
            store.background_image = self.upload_to_imgur(self.files['background_image'])

        if commit:
            store.save()

        return store

    def upload_to_imgur(self, image_file):
        """
        Faz upload de uma imagem para o Imgur e retorna a URL.
        """
        IMGUR_CLIENT_ID = "YOUR_IMGUR_CLIENT_ID"  # Substitua pelo seu CLIENT ID do Imgur
        response = requests.post(
            "https://api.imgur.com/3/upload",
            headers={"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"},
            files={"image": image_file}
        )

        if response.status_code == 200:
            return response.json().get('data', {}).get('link')
        return None




# from django import forms
# from .models import Profile
# from django.contrib.auth.models import User
# from PIL import Image
# import requests

# class RegisterForm(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES)#, widget=forms.HiddenInput(attrs={'id': 'user_type'}))
#     logo = forms.ImageField(required=False)
#     background_image = forms.ImageField(required=False)

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user', 'join_date', 'store_logo_url', 'store_background_url']

#     def save(self, commit=True):
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password']
#         )
#         profile = super().save(commit=False)
#         profile.user = user

#         # Upload images to Imgur and save URLs
#         if 'logo' in self.files:
#             profile.store_logo_url = self.upload_to_imgur(self.files['logo'])
#         if 'background_image' in self.files:
#             profile.store_background_url = self.upload_to_imgur(self.files['background_image'])

#         if commit:
#             user.save()
#             profile.save()
#         return profile

#     def upload_to_imgur(self, image_file):
#         # Add your Imgur API code here
#         response = requests.post(
#             "https://api.imgur.com/3/upload",
#             headers={"Authorization": "Client-ID YOUR_IMGUR_CLIENT_ID"},
#             files={"image": image_file}
#         )
#         if response.status_code == 200:
#             return response.json()['data']['link']
#         return None