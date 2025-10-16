from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    is_verified=models.BooleanField(default=False)
    address_line_1=models.CharField(max_length=100)
    address_line_2=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    postcode=models.CharField(max_length=10)
    country=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    profile_pic=models.ImageField(upload_to='user/profile_pic',null=True,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    username=None
    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"