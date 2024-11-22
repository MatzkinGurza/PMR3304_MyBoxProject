from django import forms
from .models import Profile
from django.contrib.auth.models import User
from PIL import Image
import requests

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES)
    logo = forms.ImageField(required=False)
    background_image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'join_date', 'store_logo_url', 'store_background_url']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        profile = super().save(commit=False)
        profile.user = user

        # Upload images to Imgur and save URLs
        if 'logo' in self.files:
            profile.store_logo_url = self.upload_to_imgur(self.files['logo'])
        if 'background_image' in self.files:
            profile.store_background_url = self.upload_to_imgur(self.files['background_image'])

        if commit:
            user.save()
            profile.save()
        return profile

    def upload_to_imgur(self, image_file):
        # Add your Imgur API code here
        response = requests.post(
            "https://api.imgur.com/3/upload",
            headers={"Authorization": "Client-ID YOUR_IMGUR_CLIENT_ID"},
            files={"image": image_file}
        )
        if response.status_code == 200:
            return response.json()['data']['link']
        return None