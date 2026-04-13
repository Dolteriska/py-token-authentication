from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        # staff може все
        if request.user and request.user.is_staff:
            return True
        # non-staff не можуть робити DELETE
        if request.method == "DELETE":
            return False
        # авторизовані — тільки read (SAFE_METHODS)
        return request.user and request.user.is_authenticated and request.method in SAFE_METHODS

