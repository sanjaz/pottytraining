from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Allows access only to admin users."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()


class IsTeacher(permissions.BasePermission):
    """Allows access only to teachers."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_teacher()


class IsAdminOrTeacher(permissions.BasePermission):
    """Allows access only to admins and teachers."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin_or_teacher()
        )
