from django.urls import path
from . import views
from .views import BoxDetailView, AddCommentView


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('box/<int:pk>', BoxDetailView.as_view(), name="box-details"),
    path('list_stores/', views.list_stores, name='list_stores'),
    path('search/', views.search_boxes, name='search_boxes'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment"),
    path('submit_review/<int:box_id>', views.submit_review, name="submit_review"),
]