from itertools import product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product,UserItem,sold,Order,mrentry,mrentryrecord,returnn,Customer
from .filters import OrderFilter,soldfilter
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Count, F, Value
from django.db import connection
from core.form import soldformm, useritem,GeeksForm,mrr,returnnform,billfrom
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.db.models import Q                              
from django.db.models import Sum
from num2words import num2words
import datetime
from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import  ListView


@login_required
def cart(request):
    form = useritem(request.POST or None, request.FILES or None)
    shopcart =UserItem.objects.filter(user=request.user)
    user_products = UserItem.objects.filter(user=request.user)
    total=0
    for gs in user_products:
        total+=gs.price1 * gs.quantity

    if form.is_valid():
        fs= form.save(commit=False)
        fs.user= request.user
        fs.invoice_id=fs.added
        
        fs.save()   
        

        for rs in shopcart:
                detail = sold()
                detail.customer    = fs.customer
                 # Order Id
                 
                detail.product_id  = rs.product_id
                detail.order_id     = fs.id 
                detail.user  = request.user
                detail.quantity  = rs.quantity
                detail.added  = rs.added
                detail.left = fs.left
                detail.discount = fs.discount
                detail.price1 = rs.price1
                detail.price2 = rs.price2
                detail.engine_no=rs.engine_no
                detail.Phone=fs.Phone
                detail.name=fs.name
                detail.sparename =rs.sparename 
                detail.save()
                
                shopcart.delete()    
                product = Product.objects.get(id=rs.product_id)
                if rs.credit =='noncredit':    
                     product.quantity -= rs.quantity
                     product.save()
        return HttpResponseRedirect("/soldlist")
        
    
    products = Product.objects.all()
   
    
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 

    # p = Paginator(products, 5)  # creating a paginator object
    # # getting the desired page number from url
    # page_number = request.GET.get('page')
    # try:
    #     page_obj = p.get_page(page_number)  # returns the desired page object
    # except PageNotAnInteger:
    #     # if page_number is not an integer then assign the first page
    #     page_obj = p.page(1)
    # except EmptyPage:
    #     # if page is empty then return last page
    #     page_obj = p.page(p.num_pages)

    
    
    # products=page_obj  
    
    paginator = Paginator(products, 20) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    pro = paginator.get_page(page_number)
    
    context = {'products': products,'myFilter':myFilter,'form':form,'user_products':user_products,'pro':pro,'total':total}
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

         orders=Order.objects.all().order_by('-id')
         myFilter =soldfilter(request.GET, queryset=orders)
         orders = myFilter.qs 
        
         context = {#'category': category,
               'orders': orders,
               'myFilter':myFilter
               }


         return render(request, 'core/soldlist.html',context)
				  
def update_view(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=id,
        )
    shopcart =UserItem.objects.filter(user=request.user,product_id=id).first()
    
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = shopcart)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "core/update_view.html", context)



def mrupdate_view(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=id,
        )
    shopcart =UserItem.objects.filter(user=request.user,product_id=id).first()
    
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = shopcart)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/mr")
 
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
                detail.discount = fs.discount
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                if rs.credit =='noncredit':    
                     product.quantity -= rs.quantity
                     product.save()

        
    obj = get_object_or_404(Product, id = id)
    products = Product.objects.all().filter(groupname=obj.groupname)
    
    
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 
	  
    context = {'products': products,'myFilter':myFilter,'form':form}
    return render(request, 'core/group.html', context)



@login_required
def cashmemo(request,id):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=sold.objects.all().filter(order_id=id)
         ordere_de=Order.objects.all().filter(id=id)
         date=Order.objects.all().filter(id=id).last()
         total=0
         for rs in orders:
            total+=rs.price1 * rs.quantity

         total1=total-date.discount
         text=num2words(total1)   
         #total = sum(product.total_price for product in self.user_products)
         context = {#'category': category,
               'orders': orders,
               'total': total,
               'text': text,
               'date': date,
               'ordere_de':ordere_de,
               'total':total,
               'total1':total1,
               }


         return render(request, 'core/cashmemo1.html',context)

@login_required
def returnno(request,id):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=sold.objects.all().filter(order_id=id)
         ordere_de=Order.objects.all().filter(id=id)
         date=sold.objects.all().filter(order_id=id).last()
         total=0
         for rs in orders:
            total+=rs.price1 * rs.quantity

         total1=total-date.discount
         text=num2words(total1)   
         #total = sum(product.total_price for product in self.user_products)
         context = {#'category': category,
               'orders': orders,
               'total': total,
               'text': text,
               'date': date,
               'ordere_de':ordere_de,
               'total':total,
               'total1':total1,
               }


         return render(request, 'core/return.html',context)




def get_total(self):
        self.total = sum(product.total_price for product in self.user_products)

                                  
def productlist(request):
    return render(request, 'core/productlist.html', {
        'products': Product.objects.all(),
    })

def mrproductlist(request):
    return render(request, 'core/mrproductlist.html', {
        'products': Product.objects.all(),
    })

def mr(request):
    form = mrr(request.POST or None, request.FILES or None)
    shopcart =UserItem.objects.filter(user=request.user)
    user_products = UserItem.objects.filter(user=request.user)
    total=0
    for gs in user_products:
        total+=gs.price1 * gs.quantity



    if form.is_valid():
        fs= form.save(commit=False)
        fs.user= request.user
        fs.invoice_id=fs.added
        
        fs.save()   
        

        for rs in shopcart:
                detail =mrentryrecord()
                detail.supplier= fs.supplier
                 # Order Id
                 
                detail.product_id  = rs.product_id
                detail.mrentry_id    = fs.id 
                detail.user  = request.user
                detail.quantity  = rs.quantity
                detail.added  = rs.added
                detail.left = fs.left
                detail.discount = fs.discount
                detail.save()
                
                shopcart.delete()    
                product = Product.objects.get(id=rs.product_id)
                if rs.credit =='noncredit':    
                     product.quantity += rs.quantity
                     product.save()

        
    
    products = Product.objects.all()
   
    
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 

    # p = Paginator(products, 5)  # creating a paginator object
    # # getting the desired page number from url
    # page_number = request.GET.get('page')
    # try:
    #     page_obj = p.get_page(page_number)  # returns the desired page object
    # except PageNotAnInteger:
    #     # if page_number is not an integer then assign the first page
    #     page_obj = p.page(1)
    # except EmptyPage:
    #     # if page is empty then return last page
    #     page_obj = p.page(p.num_pages)

    
    
    # products=page_obj  
    
    
    context = {'products': products,'myFilter':myFilter,'form':form,'user_products':user_products,'total':total}
    return render(request, 'core/mr.html', context)


def returnreasonn(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = returnn.objects.get_or_create(
           sold_id=id,
        )
    shopcart =returnn.objects.filter(sold_id=id).first()
    
    # pass the object as instance in form
    form = returnnform(request.POST or None, instance = shopcart)
 
    # save the data from the form and
    # redirect to detail_view
    #sold = sold.objects.get(id=id)
    solds = get_object_or_404(sold, id = id)
    product = Product.objects.get(id=solds.product_id)
    if form.is_valid():
        fs= form.save(commit=False)
        product.quantity += fs.quantity
        product.save()
        fs.save()
        return HttpResponseRedirect("/")
         
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "core/returnreason.html", context)


@login_required
def editcashmemo(request,id):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=sold.objects.all().filter(order_id=id)
         ordere_de=Order.objects.all().filter(id=id)
         date=sold.objects.all().filter(order_id=id).last()
         total=0
         for rs in orders:
            total+=rs.price1 * rs.quantity

         total1=total-date.discount
         text=num2words(total1) 
         products = Product.objects.all()
   
    
         myFilter = OrderFilter(request.GET, queryset=products)
         products = myFilter.qs 
         orderr =Order.objects.get(id=id)

         form = useritem(request.POST or None, request.FILES or None, instance = orderr)
         shopcart =UserItem.objects.filter(user=request.user)
         user_products = UserItem.objects.filter(user=request.user)
         total=0
         for gs in user_products:
           total+=gs.price1 * gs.quantity


         paginator = Paginator(products, 20) # Show 25 contacts per page.

         page_number = request.GET.get('page')
         pro = paginator.get_page(page_number) 

         if form.is_valid():
           fs= form.save(commit=False)
           fs.user= request.user
           fs.invoice_id=fs.added
        
           fs.save()  
        #    for rs in shopcart:
        #         detail = sold()
        #         detail.customer    = fs.customer
        #          # Order Id
                 
        #         detail.product_id  = rs.product_id
        #         detail.order_id     =id 
        #         detail.user  = request.user
        #         detail.quantity  = rs.quantity
        #         detail.added  = rs.added
        #         detail.left = fs.left
        #         detail.discount = fs.discount
        #         detail.price1 = rs.price1
        #         detail.price2 = rs.price2
        #         detail.engine_no=rs.engine_no
        #         detail.Phone=fs.Phone
        #         detail.name=fs.name
        #         detail.sparename =rs.sparename 
        #         detail.save()
                
        #         shopcart.delete()    
        #         product = Product.objects.get(id=rs.product_id)
        #         if rs.credit =='noncredit':    
        #              product.quantity -= rs.quantity
        #              product.save()

         #total = sum(product.total_price for product in self.user_products)
         context = {#'category': category,
               'orders': orders,
               'total': total,
               'text': text,
               'date': date,
               'ordere_de':ordere_de,
               'total':total,
               'total1':total1,
               'products': products,
               'myFilter':myFilter,
               'form':form,
               'user_products':user_products,
               'pro':pro

               }


         return render(request, 'core/editcashmemo.html',context)    


@login_required
def fianaleditcashmemo(request,id):
    context ={}
    shopcart =sold.objects.get(id=id)
    

    # pass the object as instance in form
    form = soldformm(request.POST or None, instance = shopcart)
    productnew = Product.objects.get(id=shopcart.product_id)
    qua=productnew.quantity+shopcart.quantity
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        fs= form.save(commit=False)
        form.save()
        #productnew.quantity  += shopcart.quantity
        
        
        productnew.quantity  = qua-fs.quantity
        productnew.save()
       
   

        
        
 
    # add form dictionary to context
    
    context["form"] = form
 
    return render(request, "core/update_view.html", context)






@login_required
def bill(request,id):
  context ={}
  form = billfrom(request.POST or None, request.FILES or None)

  if form.is_valid():
           fs= form.save(commit=False)
           fs.order_id= id
           fs.save() 
           messages.success(request, 'Form submission successful')

  context["form"] = form
  return render(request, "core/update_view.html", context)



@login_required
def customerlist(request):
    user_list = Customer.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'core/customerlist.html', { 'users': users })
        
      
  

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = Customer.objects.filter(Q(name__icontains=query)  )

    return render(request, 'core/search_results.html', {'query': query, 'users': results})
        
      