from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ("seller", "Vendedor"),
        ("buyer", "Comprador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="buyer")
    store_name = models.CharField(max_length=100, blank=True, null=True)  # Nome da loja (opcional para vendedores)
    store_image = models.ImageField(upload_to='store_images/', blank=True, null=True)  # Imagem da loja
    join_date = models.DateField(auto_now_add=True)  # Data de entrada no site
    location = models.CharField(max_length=255, blank=True, null=True)  # Localidade do usuário ou loja

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

    @property
    def is_seller(self):
        return self.user_type == "seller"

    @property
    def is_buyer(self):
        return self.user_type == "buyer"
