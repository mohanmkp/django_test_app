from django.db import models
import uuid
from apps.users.models import User



class Base_model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


category_choices = (
    ("tshirt", "tshirt"),
    ("shirt", "shirt"),
    ("mobile", "mobile"),
    ("electronic", "electronic")
)
class Product(Base_model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=255, unique=True)
    price = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    total_item = models.IntegerField()
    available_item = models.IntegerField(null=True, blank=True)
    total_sell = models.IntegerField(null=True, blank=True, default=0)
    category = models.CharField(max_length=255, null=True, blank=True, choices=category_choices)
    more_details = models.TextField(null=True, blank=True)



