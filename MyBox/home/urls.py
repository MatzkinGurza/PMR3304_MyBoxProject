from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('box/add/', views.manage_box, name='add_box'),
    path('box/edit/<int:box_id>/', views.manage_box, name='edit_box'),
]