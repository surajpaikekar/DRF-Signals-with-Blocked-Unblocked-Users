from rest_framework import permissions
from .models import BlockedUser

class IsOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_superuser


class IsNotBlocked(permissions.BasePermission):
    """
    Global permission check for blocked users.
    """

    def has_permission(self, request, view):
        user = request.user
        is_blocked = BlockedUser.objects.filter(user=user).exists()
        print(f"User {user.username} is blocked: {is_blocked}")
        return not is_blocked
