from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAuthenticated(), IsAuthorOrReadOnly()]
        return [permissions.AllowAny()]

from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow safe methods for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only author can edit/delete
        return obj.author == request.user
    
    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'error': 'User already exists or invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Only author can edit/delete
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.AllowAny()]

# Custom permission to allow only author to edit/delete
from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
    
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author__username']  # These are the fields you want users to be able to filter by

