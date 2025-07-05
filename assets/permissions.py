from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'manager']

class IsViewerReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'viewer' and request.method in ['GET']:
            return True
        return request.user.role in ['admin', 'manager']
    