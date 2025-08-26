from django.db import models
from django.contrib.auth.models import AbstractUser
from shop.models import Product

class User(AbstractUser):
    avatar = models.ImageField(upload_to="user/avatar/")
    favorite = models.ManyToManyField(Product, related_name="products")



