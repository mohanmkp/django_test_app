from rest_framework import generics
from apps.product.serializers import *
from rest_framework.response import Response
from .models import *
from custom_auth.product_permission import Product_Permission







class product_view(generics.ListCreateAPIView):
    permission_classes = [Product_Permission]
    serializer_class = product_serializer


    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        if id:
            queryset = Product.objects.filter(id=id).first()
            return Response({"title": queryset.title,
                             "price": queryset.price,
                             "total_item": queryset.total_item,
                             "available_item": queryset.available_item,
                             "image": queryset.image.url,
                             "id": queryset.id
                             })
        queryset = Product.objects.filter(is_active=True).order_by("-created_on")
        serializer = product_serializer(queryset,  many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer_data = product_serializer(data=request.data)
        if serializer_data.is_valid(raise_exception=True):
            data = dict(serializer_data.data)
            data["available_item"]= serializer_data.data["total_item"]
            data['image'] = request.data["image"]
            usr = User.objects.all().last()
            data = Product.objects.create(**data, user=usr)
            data_res = product_serializer(data)
            return Response(data_res.data)









