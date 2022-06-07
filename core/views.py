from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product,UserItem
from .filters import OrderFilter
from django.http import HttpResponse
from django.db.models import Count, F, Value
from django.db import connection
from core.form import useritem  
from django.contrib.auth.models import User

@login_required
def cart(request):
    form = useritem(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        fs= form.save(commit=False)
        fs.user= request.user
        fs.save()
        
     
    products = Product.objects.all()
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 
	  
    context = {'products': products,'myFilter':myFilter,'form':form}
    return render(request, 'core/cart.html', context)

@login_required
def dataupdate(request):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      with connection.cursor() as cursor:
        cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
        
        row = cursor.fetchone()

        
      return render(request, 'core/a.html')
                 
				  
				   

                  
                  



      


      