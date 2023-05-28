from rest_framework.permissions import IsAuthenticated



class Product_Permission(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return super().has_permission(request, view)

