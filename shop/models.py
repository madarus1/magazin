from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=101)
    desc = models.TextField()
    price = models.FloatField()
    img = models.ImageField(upload_to="imgs/product/")
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField()
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=20)
    city = models.CharField(max_length=250, blank=True, null=True)
    streat = models.CharField(max_length=250, blank=True, null=True)
    house = models.PositiveIntegerField(blank=True, null=True)
    entrance = models.PositiveIntegerField(blank=True, null=True)
    apartment = models.PositiveIntegerField(blank=True, null=True)

class OrderItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
