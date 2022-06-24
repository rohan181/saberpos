from django.contrib import admin

# Register your models here.
# 
# from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Product,UserItem,Customer,Order,sold
class OrderProductline(admin.TabularInline):
    model =sold
    
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    
    inlines = [OrderProductline]






@admin.register (Product)
class ViewAdmin(ImportExportModelAdmin):
  pass

#admin.site.register(Product,OrderAdmin)
admin.site.register(Customer,OrderAdmin)
admin.site.register(UserItem)
admin.site.register(Order)
admin.site.register(sold)