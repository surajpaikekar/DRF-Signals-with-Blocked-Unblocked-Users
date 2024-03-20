from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer, CategorySerializer, TagSerializer
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlockedUser, post, Category, Tag
from .permissions import IsOwnerOrSuperuser, IsNotBlocked
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.core.exceptions import PermissionDenied

"""
# you can add an extra action to a ModelViewSet for user registration. 
# This method is useful if you already have a ModelViewSet for users and 
# want to keep user-related actions within the same viewset.

# 1. ViewSet: Add a register action to your UserViewSet.
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# 2. URL: Ensure your ModelViewSet is included in your URL configuration.

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username=None, format=None):
        """
        Return a list of all users or a specific user.
        """
        if username:
            try:
                user = User.objects.get(username=username)
                return Response({'username': user.username, 'email': user.email})
            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=404)
        else:
            usernames = [user.username for user in User.objects.all()]
            return Response(usernames)
    
class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsNotBlocked]

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        email = EmailMessage(
            'New Post Created',
            f'A new post titled "{post.title}" has been created.',
            to=[post.author.email]
        )
        email.send()

"""
# for blocked user functionality you can create separate class in permissions.py and import here otherwise write bellow class

    def perform_create(self, serializer):
        user = self.request.user
        if BlockedUser.objects.filter(user=user).exists():
            raise PermissionDenied("You are blocked from creating posts.")
        serializer.save(author=user)
"""

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuser]

class BlockUserView(APIView):
    def post(self, request, user_id):
        blocked_user = User.objects.get(id=user_id)
        BlockedUser.objects.create(user=request.user, blocked_user=blocked_user)
        return Response(status=status.HTTP_201_CREATED)

class UnblockUserView(APIView):
    def delete(self, request, user_id):
        blocked_user = User.objects.get(id=user_id)
        BlockedUser.objects.filter(user=request.user, blocked_user=blocked_user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostFilter(filters.SearchFilter):
    def get_search_terms(self, request):
        return request.query_params.get('search', '').split()

class PostPagination(PageNumberPagination):
    page_size = 10

class PostThrottle(UserRateThrottle):
    rate = '100/hour'

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
