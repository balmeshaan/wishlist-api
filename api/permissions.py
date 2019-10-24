from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsItemOwnerOrStaff(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.user == obj.added_by or request.user.is_staff:
			return True
		return False