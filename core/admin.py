from django.contrib import admin

# Register your models here.

from .models import Product,UserItem

admin.site.register(Product)
admin.site.register(UserItem)