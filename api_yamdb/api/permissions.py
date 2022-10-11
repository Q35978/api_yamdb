# api/permissions.py
from rest_framework import permissions

from reviews.models import User


class IsAuthenticatedAndAdmin(permissions.BasePermission):
    """Проверяем является ли пользователь администратором."""
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.is_administrator
        )


class IsAuthorCanUpdateOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
            request.user == obj.author
            or request.user.is_administrator
            or request.user.is_moderator
        )


class ReadIfNotAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.role == User.ROLE_NAME_ADMIN
            )
        )
