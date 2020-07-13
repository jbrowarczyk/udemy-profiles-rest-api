from rest_framework import permissions
import pdb


class UpdateOwnProfile(permissions.BasePermission):
	"""Allow users to edit their own profile"""

	def has_object_permission(self,request,view,obj):
		"""Check user is trying to edit his own profile"""
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
	"""Allow users to edit their own status"""

	def has_object_permission(self,request,view,obj):
		"""Check the user is trying to edit their own status"""
		# pdb.set_trace()
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.user_profile_id == request.user.id