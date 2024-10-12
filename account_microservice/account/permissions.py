from rest_framework import permissions
from django.conf import settings

ADMIN_ID = 2


class IsAdmin(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return request.user.role in settings.ROLES[ADMIN_ID]
