from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView
from .views import BlockUserView, UnblockUserView
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, TagListCreateView, TagRetrieveUpdateDestroyView,ListUsers,CreateUserView


urlpatterns = [
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('api/block-user/<int:user_id>/', BlockUserView.as_view(), name='block-user'),
    path('api/unblock-user/<int:user_id>/', UnblockUserView.as_view(), name='unblock-user'),
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('api/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('api/users/create/', CreateUserView.as_view(), name='create-user'),
    path('api/users/', ListUsers.as_view(), name='list-users'),
    path('api/users/<str:username>/', ListUsers.as_view(), name='user-detail'),
    path('api/tags/<int:pk>/', TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),
]