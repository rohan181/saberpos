from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product,UserItem,sold
from .filters import OrderFilter
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Count, F, Value
from django.db import connection
from core.form import useritem,GeeksForm 
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

@login_required
def cart(request):
    form = useritem(request.POST or None, request.FILES or None)
    shopcart =UserItem.objects.filter(user=request.user)
    if form.is_valid():
        fs= form.save(commit=False)
        fs.user= request.user
        fs.save()
        

        for rs in shopcart:
                detail = sold()
                detail.customer    = fs.customer # Order Id
                detail.product_id  = rs.product_id
                detail.order_id     = fs.id 
                detail.user  = request.user
                detail.quantity  = rs.quantity
                detail.added  = rs.added
                detail.left = fs.left
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                    
                product.quantity -= rs.quantity
                product.save()

        
   
    products = Product.objects.all()
    
    
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 
    
    context = {'products': products,'myFilter':myFilter,'form':form}
    return render(request, 'core/cart.html', context)

@login_required
def soldlist(request):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=sold.objects.all().order_by('-id')
         context = {#'category': category,
               'orders': orders,
               }


         return render(request, 'core/a.html',context)
				  
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "core/update_view.html", context)



def ggroup(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "core/update_view.html", context)	




@login_required
def group(request,id):
    form = useritem(request.POST or None, request.FILES or None)
    shopcart =UserItem.objects.filter(user=request.user)
    if form.is_valid():
        fs= form.save(commit=False)
        fs.user= request.user
        fs.save()
        

        for rs in shopcart:
                detail = sold()
                detail.customer    = fs.customer # Order Id
                detail.product_id  = rs.product_id
                detail.user  = request.user
                detail.quantity  = rs.quantity
                detail.added  = rs.added
                detail.left = fs.left
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                    
                product.quantity -= rs.quantity
                product.save()

        
    obj = get_object_or_404(Product, id = id)
    products = Product.objects.all().filter(groupname=obj.groupname)
    
    
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 
	  
    context = {'products': products,'myFilter':myFilter,'form':form}
    return render(request, 'core/group.html', context)





                  
                  



      


      