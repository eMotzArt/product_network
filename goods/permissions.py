from rest_framework import permissions
from rest_framework.request import Request

class IsActive(permissions.BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        return request.user.is_active
