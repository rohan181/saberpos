from django.contrib import admin

# Register your models here.
# 
# from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product,UserItem,Customer,Order,sold,mrentryrecord,supplier,mrentry,returnn,bill,paybill,paybillcatogory
class OrderProductline(admin.TabularInline):
    model =sold
    
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    
    inlines = [OrderProductline]

class PhotoAdmin(admin.ModelAdmin):
  
    search_fields = ['name']




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
admin.site.register(mrentryrecord)
admin.site.register(mrentry)
admin.site.register(Order)
admin.site.register(supplier)
admin.site.register(sold,ComputerAdmin)
admin.site.register(returnn)
admin.site.register(paybill)
admin.site.register(paybillcatogory)
admin.site.register(bill)


class SwitchModelResource(resources.ModelResource):
        class Meta:
            model = Product
    

class SwitchModelAdmin(ImportExportModelAdmin):
        list_display = ('added', 'name')
        list_filter=('added','productcatagory')
        resource_class = SwitchModelResource
        inlines = [OrderProductline]
        search_fields = ['name']

admin.site.register(Product,SwitchModelAdmin)
