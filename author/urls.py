from django.urls import path
from .views import *

urlpatterns = [
    path("sing_up/", sign_up, name="sing_up"),
    path("log_in/", log_in, name="log_in"), 
    path("exit/", exit, name="exit"),
    path("profile", profile, name="profile"),
]