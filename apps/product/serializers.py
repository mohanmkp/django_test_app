from rest_framework import serializers
from apps.product.models import Product



class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'total_item', 'image', "category",
                  "available_item", "total_sell", "is_active", "more_details"

                  ]








