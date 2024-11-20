from django.urls import path
from . import views
from .views import BoxDetailView, AddBoxView, UpdateBoxView, DeleteBoxView

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('box/add/', views.manage_box, name='add_box'),
    path('box/edit/<int:box_id>/', views.manage_box, name='edit_box'),
    path('box/<int:pk>', BoxDetailView.as_view(), name="box-detail"),
    path('add_box/', AddBoxView.as_view(), name='add_box'),
    path('box/update/<int:pk>', UpdateBoxView.as_view(), name='update_box'),
    path('box/<int:pk>/delete', DeleteBoxView.as_view(), name='delete_box'),
]