from django.contrib.auth.models import User
from django.db import models

# Modelo de Perfil para Usuários
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ("seller", "Vendedor"),
        ("buyer", "Comprador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null =True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    # Campos para usuários
    cpf = models.CharField(max_length=14, unique=False, blank=False, null=False, default="000.000.000-00")  # CPF genérico
    phone = models.CharField(max_length=15, blank=False, null=False, default="(00) 00000-0000")  # Telefone padrão genérico
    address = models.TextField(blank=False, null=False, default="Endereço não informado")  # Endereço padrão
    complement = models.CharField(max_length=100, blank=True, null=True, default="Nenhum complemento")  # Complemento padrão
    cep = models.CharField(max_length=10, blank=False, null=False, default="00000-000")  # CEP padrão genérico
    birth_date = models.DateField(blank=False, null=False, default="2000-01-01")  # Data de nascimento padrão

    join_date = models.DateField(auto_now_add=True)  # Data de criação do perfil

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

    @property
    def is_seller(self):
        return self.user_type == "seller"

    @property
    def is_buyer(self):
        return self.user_type == "buyer"


# Modelo de Loja para Vendedores
class Store(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    store_name = models.CharField(max_length=100, blank=False, null=False)
    store_email = models.EmailField(unique=True, blank=False, null=False)  # Email único para a loja
    cnpj = models.CharField(max_length=18, unique=True, blank=False, null=False)  # CNPJ único
    logo_url = models.URLField(blank=True, null=True) # Logo da loja
    background_url = models.URLField(blank=True, null=True) # Imagem de fundo
    store_description = models.TextField(max_length=200, blank=True, null=True)  # Descrição da loja

    def __str__(self):
        return self.store_name


# class Profile(models.Model):
#     USER_TYPE_CHOICES = [
#         ("seller", "Vendedor"),
#         ("buyer", "Comprador"),
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="buyer")
    
#     # Fields for sellers
#     store_name = models.CharField(max_length=100, blank=True, null=True)
#     cnpj = models.CharField(max_length=18, blank=True, null=True)
#     cpf = models.CharField(max_length=14, blank=True, null=True)
#     store_email = models.EmailField(blank=True, null=True)
#     store_phone = models.CharField(max_length=15, blank=True, null=True)
#     store_address = models.TextField(blank=True, null=True)
#     store_description = models.TextField(max_length=200, blank=True, null=True)
#     store_logo_url = models.URLField(blank=True, null=True)
#     store_background_url = models.URLField(blank=True, null=True)

#     # Fields for buyers
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     birth_date = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=50, blank=True, null=True)
#     buyer_cpf = models.CharField(max_length=14, blank=True, null=True)
#     buyer_email = models.EmailField(blank=True, null=True)
#     buyer_phone = models.CharField(max_length=15, blank=True, null=True)
#     buyer_address = models.TextField(blank=True, null=True)

#     join_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.get_user_type_display()}"

#     @property
#     def is_seller(self):
#         return self.user_type == "seller"

#     @property
#     def is_buyer(self):
#         return self.user_type == "buyer"


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
