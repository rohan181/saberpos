from django.contrib import admin

# Register your models here.
# 
# from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product,UserItem,Customer,Order,sold
class OrderProductline(admin.TabularInline):
    model =sold
    
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    
    inlines = [OrderProductline]



class ComputerAdmin(admin.ModelAdmin):
    list_filter=('added', 'product')
    list_display = ('added', 'product')
    search_fields=('added', 'product') 


#@admin.register (Product)
#class ViewAdmin(ImportExportModelAdmin):
  #pass

#admin.site.register(Product,OrderAdmin)
admin.site.register(Customer,OrderAdmin)
admin.site.register(UserItem)

admin.site.register(Order)
admin.site.register(sold,ComputerAdmin)
class SwitchModelResource(resources.ModelResource):
        class Meta:
            model = Product
    

class SwitchModelAdmin(ImportExportModelAdmin):
        list_display = ('added', 'name')
        list_filter=('added','productcatagory')
        resource_class = SwitchModelResource
        inlines = [OrderProductline]

admin.site.register(Product,SwitchModelAdmin)
