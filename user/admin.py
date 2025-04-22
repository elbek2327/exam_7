from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser


# Register your models here.
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('id', 'email','phone_number', 'is_active', 'is_superuser')