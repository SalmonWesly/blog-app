from django.urls import path
from .views import BlogListCreate, BlogDetail

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]
from django.urls import path
from .views import register_user

urlpatterns = [
    path('api/register/', register_user, name='register'),
]
from django.urls import path
from .views import BlogListCreateView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]