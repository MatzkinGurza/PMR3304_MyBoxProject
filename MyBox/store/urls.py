from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Página do vendedor
    path('<int:seller_id>/', views.store_page, name='store_page'),
]
