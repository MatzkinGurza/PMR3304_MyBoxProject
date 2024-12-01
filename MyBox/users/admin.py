from django.contrib import admin
from .models import Profile, Store, Cart, CartItem, Subscription, Payment
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Campos exibidos na lista do admin
    list_display = ('user', 'tipo_de_usuário', 'join_date')  # Atualizado para campos existentes no modelo
    list_filter = ('tipo_de_usuário', 'join_date')  # Filtros baseados nos campos válidos
    search_fields = ('user__username', 'user__email')  # Permitindo busca por nome de usuário e e-mail do User

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    # Campos exibidos na lista do admin para lojas
    list_display = ('store_name', 'store_email', 'cnpj', 'owner')  # Ajustado para refletir o modelo Store
    list_filter = ('store_name', 'cnpj')  # Filtros aplicados ao admin de lojas
    search_fields = ('store_name', 'store_email', 'cnpj')  # Permitindo busca por nome da loja, e-mail e CNPJ

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Subscription)
admin.site.register(Payment)

# from django.contrib import admin
# from .models import Profile

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'user_type', 'store_address', 'store_name', 'join_date')  # Replaced 'location' with 'store_address'
#     list_filter = ('user_type', 'join_date')
#     search_fields = ('user__username', 'store_name')
