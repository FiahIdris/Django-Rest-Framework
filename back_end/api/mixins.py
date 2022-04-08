from .permissions import IsStaffEditorPermission
from rest_framework import permissions

class StafEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]