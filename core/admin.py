from django.contrib import admin

# Register your models here.

from .models import Product,UserItem,Customer,Order
# class OrderProductline(admin.TabularInline):
#     model =Order
    
#     extra = 0

# class OrderAdmin(admin.ModelAdmin):
    
#     inlines = [OrderProductline]



admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(UserItem)
admin.site.register(Order)