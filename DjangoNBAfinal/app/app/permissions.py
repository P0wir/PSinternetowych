from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyOrAdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_superuser

class ReadOnlyOrStaff(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff

class CreateOrAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'