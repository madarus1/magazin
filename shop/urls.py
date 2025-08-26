from django.urls import path
from .views import *

urlpatterns = [
    path("", catolog, name="main"),
    path("product_detail/<int:product_id>/", product_detail, name="barashek"),
    path("basket/", basket, name="basket"),
    path("basket/add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("basket/remove/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("basket/reduce/<int:product_id>/", reduce_from_cart, name="reduce_from_cart"),
    path("basket/basket/", basket, name="basket"),
    path("favorite/<int:product_id>/", favorite_products, name="favorite_products")
    
]