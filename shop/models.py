from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=101)
    desc = models.TextField()
    price = models.FloatField()
    img = models.ImageField(upload_to="imgs/product/")
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

# class Order(models.Model):
#     product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=250)
#     created_at = models.DateTimeField(auto_now_add=True)




