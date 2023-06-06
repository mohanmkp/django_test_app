from apps.orders.serializers import *
from apps.orders.models import OrdersDetails



class OderSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(max_length=255)
    class Meta:
        model = OrdersDetails
        fields = [
            "product_id",
            "deliver_charge",
            "delivery_address",
            "alter_phone",
            "payment_method",
            "no_of_items",

        ]





