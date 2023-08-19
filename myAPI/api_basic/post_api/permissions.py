from email import message
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message='Inauthorized access denied. Only owners or supervisors are permitted. (Source: Post_API)'
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.author == request.user or request.user.is_superuser)

#objenin sahibi degilse silme ya da edit yapamasin, eger admin ise guncelleyebilsin.