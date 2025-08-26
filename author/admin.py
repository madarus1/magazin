from django.contrib import admin
from author.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass