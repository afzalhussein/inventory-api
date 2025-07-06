from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']

class IsViewerReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow authenticated users with role='viewer' to GET
        if request.user.is_authenticated:
            return request.user.role == 'viewer' and request.method in ['GET']
        
        # Anonymous users are not allowed
        return False

# Uncomment the following code if you want to allow GET requests for anonymous users
# class IsViewerReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             # Allow GET for authenticated viewers or anonymous users
#             if request.user.is_authenticated:
#                 return request.user.role == 'viewer' or request.user.role in ['admin', 'manager']
#             return True  # Allow anonymous read access
#         return request.user.is_authenticated and request.user.role == 'viewer'