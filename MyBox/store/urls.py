from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('<int:box_id>/manage/', views.manage_box, name='manage_box'),  # Rota para gerenciar uma Box específica
    path('add/', views.manage_box, name='manage_box'),  # Rota para adicionar uma nova Box
    path('<int:seller_id>/', views.store_page, name='store_page'),  # Rota para a página da loja
]
