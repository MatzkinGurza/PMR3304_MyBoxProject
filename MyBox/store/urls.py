from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('manage_box/<int:box_id>/', views.manage_box, name='manage_box'),  # Gerenciar uma Box existente
    path('store_page/<int:seller_id>/', views.store_page, name='store_page'),  # Página do vendedor
    path('box/<int:pk>/', views.BoxDetailView.as_view(), name="box-detail"),  # Detalhes de uma Box
    path('add_box/', views.AddBoxView.as_view(), name='add_box'),  # Adicionar uma nova Box
    path('box/update/<int:pk>/', views.UpdateBoxView.as_view(), name='update_box'),  # Atualizar uma Box
    path('box/<int:pk>/delete/', views.DeleteBoxView.as_view(), name='delete_box'),  # Excluir uma Box
    path('not_seller/', views.not_seller, name='not_seller'),   # Página informativa para buyers
]
