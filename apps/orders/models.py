from django.db import models
from apps.product.models import Base_model, Product
from apps.users.models import User





class ProdictOrder(Base_model):
    payment_method_list = (
        ("cash", "cash"),
        ("upi", "upi")
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deliver_charge = models.IntegerField()
    delivery_address = models.TextField()
    alter_phone = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=255, choices=payment_method_list)
    is_delivered = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    no_of_items = models.IntegerField()



