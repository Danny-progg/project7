from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().author


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

        return False


class IsEducator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoles.EDUCATOR
