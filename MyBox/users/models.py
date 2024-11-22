from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ("seller", "Vendedor"),
        ("buyer", "Comprador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="buyer")
    
    # Fields for sellers
    store_name = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    store_email = models.EmailField(blank=True, null=True)
    store_phone = models.CharField(max_length=15, blank=True, null=True)
    store_address = models.TextField(blank=True, null=True)
    store_description = models.TextField(max_length=200, blank=True, null=True)
    store_logo_url = models.URLField(blank=True, null=True)
    store_background_url = models.URLField(blank=True, null=True)

    # Fields for buyers
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    buyer_cpf = models.CharField(max_length=14, blank=True, null=True)
    buyer_email = models.EmailField(blank=True, null=True)
    buyer_phone = models.CharField(max_length=15, blank=True, null=True)
    buyer_address = models.TextField(blank=True, null=True)

    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

    @property
    def is_seller(self):
        return self.user_type == "seller"

    @property
    def is_buyer(self):
        return self.user_type == "buyer"


# class Profile(models.Model):
#     USER_TYPE_CHOICES = [
#         ("seller", "Vendedor"),
#         ("buyer", "Comprador"),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="buyer")
#     store_name = models.CharField(max_length=100, blank=True, null=True)  # Nome da loja (opcional para vendedores)
#     store_image = models.ImageField(upload_to='store_images/', blank=True, null=True)  # Imagem da loja
#     # store_image = models.URLField(blank=True, null=True)
#     join_date = models.DateField(auto_now_add=True)  # Data de entrada no site
#     location = models.CharField(max_length=255, blank=True, null=True)  # Localidade do usuário ou loja

#     def __str__(self):
#         return f"{self.user.username} - {self.get_user_type_display()}"

#     @property
#     def is_seller(self):
#         return self.user_type == "seller"

#     @property
#     def is_buyer(self):
#         return self.user_type == "buyer"
