from django.urls import path
from .views import catolog

urlpatterns = [
    path("", catolog)
]