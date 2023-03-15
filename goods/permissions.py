from rest_framework import permissions
from rest_framework.request import Request

from core.models import User


class IsFactory(permissions.BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        return request.user.role == User.Role.factory

class IsAgent(permissions.BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        return request.user.role in [User.Role.trader, User.Role.retailer]