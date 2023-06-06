from rest_framework import generics, status
from apps.product.models import Product
from .serializers.order import OderSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response





class OrderProduct(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = OderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)

            return Response("ok")




