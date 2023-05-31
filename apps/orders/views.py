from rest_framework import generics, status
from .models import ProdictOrder
from .serializers.order import OderSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response





class OrderProduct(generics.ListCreateAPIView):
    permission_classes = [AllowAny]


    def post(self, request, *args, **kwargs):
        serializer = OderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)

            return Response("ok")


