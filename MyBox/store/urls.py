from django.urls import path
from . import views
from .views import BoxDetailView, AddBoxView, UpdateBoxView, DeleteBoxView

app_name = 'store'

urlpatterns = [
    path('<int:box_id>/manage/', views.manage_box, name='manage_box'),  # Rota para gerenciar uma Box específica
    path('add/', views.manage_box, name='manage_box'),  # Rota para adicionar uma nova Box
    path('<int:seller_id>/', views.store_page, name='store_page'),  # Rota para a página da loja
    path('box/<int:pk>', BoxDetailView.as_view(), name="box-detail"),
    path('add_box/', AddBoxView.as_view(), name='add_box'),
    path('box/update/<int:pk>', UpdateBoxView.as_view(), name='update_box'),
    path('box/<int:pk>/delete', DeleteBoxView.as_view(), name='delete_box'),
]
