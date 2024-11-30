from django.urls import path
from . import views
from .views import BoxDetailView


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('box/<int:pk>', BoxDetailView.as_view(), name="box-details"),
    path('list_stores/', views.list_stores, name='list_stores'),
    path('search/', views.search_boxes, name='search_boxes'),
]