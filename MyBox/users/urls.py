from django.urls import path
from . import views
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, CreateProfileView, CreateStoreView, AddToCartView, CartDetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


app_name = 'users'

urlpatterns = [
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name="user_profile"),
    path('password/', PasswordsChangeView.as_view(template_name='users/change-password.html')),
    # path('login/', views.login_view, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('logout/', views.logout_view, name='logout'),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
    path('create_store', CreateStoreView.as_view(), name="create_store"),
    path('add/<int:box_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartDetailView.as_view(), name='detail'),
]
