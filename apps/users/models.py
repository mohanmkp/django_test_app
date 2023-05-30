from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid




class UserManager(BaseUserManager):
    def create_superuser(self, email, password, mobile_number):

        user = self.model(
            email=email,
            password=password,
            mobile_number=mobile_number
        )

        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, profile_pic, password, email, gender, mobile_number):

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            profile_pic=profile_pic,
            email=email,
            gender=gender,
            mobile_number=mobile_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profile_pic = models.FileField(upload_to="profile", null=True, blank=True)
    gender = models.BooleanField(default=False)
    mobile_number = models.BigIntegerField(unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password", "mobile_number"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser



class Customer_Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    trademark = models.TextField()
    house_number = models.CharField(max_length=255)
    address = models.TextField()
    pincode = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)



