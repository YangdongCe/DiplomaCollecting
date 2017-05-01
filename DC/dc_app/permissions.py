from rest_framework import permissions
'''
class IsPostOrIsAuthenticated(permissions.BasePermission):        

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated()
'''
from rest_framework import permissions
class IsSuperOrReadOnly(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif request.user.is_superuser:
			return True
		return False
