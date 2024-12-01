from django.contrib.auth.models import User
from django.db import models
from store.models import Box
<<<<<<< HEAD
=======
from django.urls import reverse
>>>>>>> carrinho

# Modelo de Perfil para Usuários
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ("seller", "Vendedor"),
        ("buyer", "Comprador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null =True)
    tipo_de_usuário = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    # Campos para usuários
    CPF = models.CharField(max_length=14, unique=False, blank=False, null=False, default="000.000.000-00")  # CPF genérico
    telefone = models.CharField(max_length=15, blank=False, null=False, default="(00) 00000-0000")  # Telefone padrão genérico
    endereço = models.TextField(blank=False, null=False, default="Endereço não informado")  # Endereço padrão
    complemento = models.CharField(max_length=100, blank=True, null=True, default="Nenhum complemento")  # Complemento padrão
    CEP = models.CharField(max_length=10, blank=False, null=False, default="00000-000")  # CEP padrão genérico
    nascimento = models.DateTimeField(blank=False, null=False, default="2000-01-01")  # Data de nascimento padrão

    join_date = models.DateTimeField(auto_now_add=True)  # Data de criação do perfil

    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_de_usuário_display()}"

    @property
    def is_seller(self):
        return self.tipo_de_usuário == "vendedor"

    @property
    def is_buyer(self):
        return self.tipo_de_usuário == "comprador"


# Modelo de Loja para Vendedores
class Store(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    store_name = models.CharField(max_length=100, blank=False, null=False)
    store_email = models.EmailField(unique=True, blank=False, null=False)  # Email único para a loja
    cnpj = models.CharField(max_length=18, unique=True, blank=False, null=False)  # CNPJ único
    logo_url = models.URLField(blank=True, null=True) # Logo da loja
    background_url = models.URLField(blank=True, null=True) # Imagem de fundo
    store_description = models.TextField(max_length=200, blank=True, null=True)  # Descrição da loja

    def get_related_boxes(self):
        # Retorna todas as Boxes associadas ao vendedor dessa loja
        return Box.objects.filter(seller=self.owner.user)

    def __str__(self):
        return self.store_name

# Modelo de Carrinho
class Cart(models.Model):
    buyer = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="cart",
        null=True,
        blank=True
    )  # Um comprador pode ter apenas um carrinho
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do carrinho
    updated_at = models.DateTimeField(auto_now=True)  # Data da última atualização

    def __str__(self):
        return f"Carrinho de {self.buyer.username}" 
    
    @property
    def total_price(self):
        """Calcula o preço total de todos os itens no carrinho."""
        return sum(item.total_price for item in self.cart_items.all())

    def get_absolute_url(self):
        """Redireciona para a visualização do carrinho."""
        return reverse('cart:detail', kwargs={'cart_id': self.id})
    
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE, 
        related_name="cart_items"
    )  # Um carrinho pode ter vários itens
    box = models.ForeignKey(
        Box, 
        on_delete=models.CASCADE
    )  # Cada item está relacionado a uma Box específica
    quantity = models.PositiveIntegerField(default=1)  # Quantidade do item no carrinho

    def __str__(self):
        return f"{self.quantity}x {self.box.name} no carrinho de {self.cart.buyer.username}"

    @property
    def total_price(self):
        """Calcula o preço total deste item (quantidade x preço da Box)."""
        return self.quantity * self.box.price

class Payment(models.Model):
    box = models.ForeignKey(
        CartItem,
        on_delete=models.CASCADE,
        related_name="selected_box"
    )  
    nome_no_cartão = models.CharField(max_length=255, null=True, blank=True)
    número_do_cartão = models.BigIntegerField(null=True, blank=True)
    validade = models.DateField(null=True, blank=True)
    CPF_do_titular = models.BigIntegerField(null=True, blank=True)
    PIN = models.IntegerField(null=True, blank=True)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name="subscription")
    purchase_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Subscrição {self.id} - {self.user.username}"


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
