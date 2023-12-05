from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Product, Category

admin.site.register(MyUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Category)
