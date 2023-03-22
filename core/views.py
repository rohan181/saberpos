from itertools import product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product,UserItem,sold,Order,mrentry,mrentryrecord,returnn,Customer,dailyreport,paybillcatogory,temppaybill,paybill,bill,mrentryrecord
from .filters import OrderFilter,soldfilter,dailyreportfilter,expensefilter,paybillfilter
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Count, F, Value
from django.db import connection
from core.form import soldformm, useritem,GeeksForm,mrr,returnnform,billfrom,dailyreportt,tempbilformm
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
from twilio.rest import Client 
from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import  ListView
from django.urls import reverse
from dal import autocomplete


@login_required
def cart(request):
    
    a =UserItem.objects.filter(user=request.user).last()
    form = useritem(request.POST or None, request.FILES or None)
    form2 = GeeksForm(request.POST or None, request.FILES or None,instance = a)
    shopcart =UserItem.objects.filter(user=request.user)
    user_products = UserItem.objects.filter(user=request.user,groupproduct =False)
   
    total=0
    total1=0
    for gs in user_products:
        total+=gs.price1 * gs.quantity
    for gs in user_products:
        total1+=gs.price1 * gs.quantity    
    outstock=1    
    
    if request.method=='POST' and 'btnform1' in request.POST: 
      if form2.is_valid() :
        fs = form2.save(commit=False)
        fs.user= request.user 
    
        fs.groupproduct=False
        fs.save()
        obj = get_object_or_404(Product, id = fs.product_id)
        products = Product.objects.all().filter(groupname=obj.groupname).exclude(groupname='')
       
        for rs in products: 
          item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=rs.id,
            groupproduct = True,
            quantity=rs.subpartquantity * fs.quantity

          )

        return HttpResponseRedirect("/")
     

    # for rs in shopcart:
    #     product = Product.objects.get(id=rs.product_id)
    #     if product.quantity < rs.quantity and rs.credit =='noncredit':
    #                 outstock=0   
    if request.method=='POST' and 'btnform2' in request.POST: 
     if form.is_valid() and outstock==1:
        fs= form.save(commit=False)
        fs.user= request.user
        fs.totalprice=total-fs.discount
        fs.totalprice1=total1-fs.discount
        fs.due=total-(fs.paid+fs.discount)
        fs.invoice_id=fs.added

        
        fs.save()
        if fs.customer !=None:
          cus =Customer.objects.filter(id=fs.customer_id).first()
          cus.balance +=fs.due
          cus.save()
        
        obj = dailyreport.objects.all().last()
        item, created =dailyreport.objects.get_or_create(
            order_id=fs.id,
            ammount=obj.ammount+fs.paid,
            petteyCash=obj.petteyCash,
            reporttype='INVOICE'
            
        )
           
        

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
                detail.remarks =rs.remarks
                detail.sparename =rs.sparename 
                detail.groupproduct = rs.groupproduct
                
                
                shopcart.delete()    
                user_products.delete()
                product = Product.objects.get(id=rs.product_id)
                product.quantity -= rs.quantity
                detail.exchange_ammount=rs.exchange_ammount
                detail.costprice=product.price
                detail.save()
                product.save()
                

                
        
          
            
        return HttpResponseRedirect("/soldlist")

      
        
    
    products = Product.objects.all()

    totalbalnce=0
    for p in products:
        totalbalnce +=p.price * p.quantity

    mo = Product.objects.filter(mother=True)

    bl=0
    for p in mo:
        bl +=p.price * p.quantity    
    totalbalnce=totalbalnce-bl
    
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
    
    paginator = Paginator(products, 200) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    pro = paginator.get_page(page_number)


    
    context = {'products': products,'myFilter':myFilter,'form':form,'user_products':user_products,'pro':pro,'total':total,'totalbalace':totalbalnce,'form2':form2}
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


def mrlist(request):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=mrentry.objects.all().order_by('-id')
         #myFilter =soldfilter(request.GET, queryset=orders)
         #orders = myFilter.qs 
        
         context = {#'category': category,
               'orders': orders,
               #'myFilter':myFilter
               }


         return render(request, 'core/mrlist.html',context)
				  
def update_view(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=id,
            groupproduct = False
        )
    shopcart =UserItem.objects.filter(user=request.user,product_id=id).first()
    obj = get_object_or_404(Product, id = id)
    products = Product.objects.all().filter(groupname=obj.groupname,mother=True).first()
   
    
    

    
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = shopcart)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        fs= form.save(commit=False)
        fs.save()
        if fs.enginecomplete =="complete":
            products.quantity = products.quantity-1
            products.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "core/update_view.html", context)



def addproduct(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=id,
            groupproduct = False
        )

    #obj = get_object_or_404(Product, id = id,mother=True)
   

      
    
   
    
    return HttpResponseRedirect("/") 

  

def addproductgroup(request,id):
    # dictionary for initial data with
    # field names as keys
    

    #obj = get_object_or_404(Product, id = id,mother=True)
    obj = get_object_or_404(Product, id = id)
    products = Product.objects.all().filter(groupname=obj.groupname)
    for rs in products: 
        item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=rs.id,
            groupproduct = True,
            quantity=rs.quantity

        )

      
    
   
    
    return HttpResponseRedirect("/") 



def expenseform(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = temppaybill.objects.get_or_create(
            user_id=request.user.id,
            paybillcatogory_id=id,
           
        )
    shopcart =temppaybill.objects.filter(user=request.user,paybillcatogory_id=id).first()
    obj = get_object_or_404(Product, id = id)
   
   
    
    

    
    # pass the object as instance in form
    form = tempbilformm(request.POST or None, instance = shopcart)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        fs= form.save(commit=False)
        fs.save()
        
        return HttpResponseRedirect("/expense")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "core/update_view.html", context)





def groupupdate_view(request,id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    #obj = get_object_or_404(Product, id = id)
    
    item, created = UserItem.objects.get_or_create(
            user_id=request.user.id,
            product_id=id,
            groupproduct=True
        )
    shopcart =UserItem.objects.filter(user=request.user,product_id=id).first()

    obj = get_object_or_404(Product, id = id)
    products = Product.objects.all().filter(groupname=obj.groupname,mother=True).first()
    
    mother =UserItem.objects.filter(user=request.user,product_id=products.id).first()


   
   

    
    
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = shopcart)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        fs= form.save(commit=False)
        mother.price1 +=fs.price1 * fs.quantity
        mother.price2 +=fs.price2 * fs.quantity
        
        
        fs.save()
        mother.save()
        if fs.enginecomplete =="complete":
            products.quantity = products.quantity-1
        products.save()
        return HttpResponseRedirect("group")
 
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
    user_products = UserItem.objects.filter(user=request.user)
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
	  
    context = {'products': products,'myFilter':myFilter,'user_products':user_products}
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

         orders=sold.objects.all().filter(order_id=id,groupproduct =False)
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
def cashmemo1(request,id):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=sold.objects.all().filter(order_id=id,groupproduct =False)
         ordere_de=Order.objects.all().filter(id=id)
         date=Order.objects.all().filter(id=id).last()
         total=0
         for rs in orders:
            total+=rs.price2 * rs.quantity

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


         return render(request, 'core/cashmemo2.html',context)


@login_required
def chalan(request,id):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=sold.objects.all().filter(order_id=id,groupproduct =False)
         ordere_de=Order.objects.all().filter(id=id)
         date=Order.objects.all().filter(id=id).last()
         total=0
         for rs in orders:
            total+=rs.price2 * rs.quantity

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


         return render(request, 'core/chalan.html',context)    


@login_required
def chalan(request,id):
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
            total+=rs.price2 * rs.quantity

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


         return render(request, 'core/chalan.html',context)                      


@login_required
def mrmemo(request,id):
      #cursor = connection['db.sqlite3'].cursor()
      #user_products = Product.objects.raw("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
      #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM core_useritem WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_useritem WHERE product_id = core_product.id)")
     
      #with connection.cursor() as cursor:
       # cursor.execute("INSERT INTO core_sold SELECT * FROM core_useritem ")
        #cursor.execute("UPDATE core_product SET quantity =core_product.quantity-(SELECT quantity FROM  core_sold WHERE product_id = core_product.id) where EXISTS (SELECT quantity FROM core_sold WHERE product_id = core_product.id) ")
        #cursor.execute("UPDATE  core_sold  SET quantityupdate=1")
        
        #row = cursor.fetchone()

         orders=mrentryrecord.objects.all().filter(mrentry_id=id,groupproduct =False)
         ordere_de=Order.objects.all().filter(id=id)
         date=mrentry.objects.all().filter(id=id).last()
         total=0
         for rs in orders:
            total+=rs.price1 * rs.quantity

         total1=total
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


         return render(request, 'core/mrmemo.html',context)

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
                detail.price1=fs.price1
                detail.discount = fs.discount
                detail.save()
                
                shopcart.delete()    
                product = Product.objects.get(id=rs.product_id)
                if rs.credit =='noncredit':    
                     product.quantity += rs.quantity
                     product.price = rs.price1
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
        obj = dailyreport.objects.all().last()
        item, created =dailyreport.objects.get_or_create(
            returnn_id=fs.id,
            ammount=obj.ammount-solds.price1,
            returnprice=solds.price1*solds.quantity
        )

        
        return HttpResponseRedirect("/")
         
    # add form dictionary to context
    context["form"] = form
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


         total1=0
         
         for gs in user_products:
           total1+=gs.price1 * gs.quantity   


         paginator = Paginator(products, 20) # Show 25 contacts per page.

         page_number = request.GET.get('page')
         pro = paginator.get_page(page_number) 

         if form.is_valid():
           fs= form.save(commit=False)
           fs.user= request.user
           
           fs.invoice_id=fs.added
           fs.totalprice=total-fs.discount
           fs.totalprice1=total1-fs.discount
           fs.due=total-(fs.paid+fs.discount)
           fs.invoice_id=fs.added
        
           fs.save()  
           for rs in shopcart:
                detail = sold()
                detail.customer    = fs.customer
                 # Order Id
                 
                detail.product_id  = rs.product_id
                detail.order_id     =id 
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
                detail.groupproduct = rs.groupproduct

                detail.save()
                
                shopcart.delete()    
                product = Product.objects.get(id=rs.product_id)
                if rs.credit =='noncredit':    
                     product.quantity -= rs.quantity
                     product.save()

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
def billt(request,id):
  context ={}
  form = billfrom(request.POST or None, request.FILES or None)

  if form.is_valid():
           fs= form.save(commit=False)
           fs.order_id= id
           fs.save() 
           obj = dailyreport.objects.all().last()
           messages.success(request, 'Form submission successful')
           item, created =dailyreport.objects.get_or_create(
            bill_id=fs.id,
            ammount=obj.ammount+fs.ammount
            
            )

  context["form"] = form
  return render(request, "core/update_view.html", context)



@login_required
def customerlist(request):
    user_list = Customer.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 20)
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
        
      

@login_required
def customersolddeatails(request):
    user_list = Customer.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'core/customerlist.html', { 'users': users })   




@login_required
def billcustomer(request,id):
  context ={}
  form = billfrom(request.POST or None, request.FILES or None)
  cus = Customer.objects.get(id=id)

  if form.is_valid():
           fs= form.save(commit=False)
           fs.customer_id=id
           fs.save() 
           cus.balance  -= fs.ammount
           cus.save()
           obj = dailyreport.objects.all().last()
           item, created =dailyreport.objects.get_or_create(
            bill_id=fs.id,
            ammount=obj.ammount+fs.ammount
            
            )
           
           messages.success(request, 'Form submission successful')

  context["form"] = form
  return render(request, "core/update_view.html", context)


def dalyreport(request):

         orders=dailyreport.objects.all().order_by('id')
         myFilter =dailyreportfilter(request.GET, queryset=orders)
         orders = myFilter.qs 

         
         paginator = Paginator(orders, 15) # Show 25 contacts per page.

         page_number = request.GET.get('page')
         orders = paginator.get_page(page_number)
         cashsale=0
         duesale=0
         netsale=0
         salesreturn=0
         collection=0
         expension=0
        
         orderlist=Order.objects.all()
         for rs in orders:
           for invoice in orderlist:
              if invoice.id == rs.order_id :
                cashsale =cashsale + invoice.paid
           
    
         
                      



        
         context = {#'category': category,
               'orders': orders,
               'myFilter':myFilter,
                'cashsale':cashsale,
                'duesale':duesale,
                'netsale':netsale,
                'salesreturn':salesreturn,
                'collection':collection,
                'expension' :expension,
               }


         return render(request, 'core/daily-report.html',context)



def dalyreportsearch(request):
    
    return render(request, "core/a.html")    

def expense(request):

         orders=dailyreport.objects.all().last()
         lastpaybill=paybill.objects.all().last()
         #myFilter =dailyreportfilter(request.GET,queryset=orders)
         user_products = temppaybill.objects.filter(user=request.user)
         form = dailyreportt(request.POST or None, request.FILES or None)
         total=0
        
         for gs in user_products:
           total+=gs.ammount 
         if request.method=='POST' and 'btnform1' in request.POST:
           
           if form.is_valid() :
           
             fs = form.save(commit=False)
             item, created =paybill.objects.get_or_create(

             pettycashbalance=orders.petteyCash +fs.petteyCash,
             reloadpetteycash=fs.petteyCash,
             typecat="receive"
             )
             fs.billexpense = fs.petteyCash
             fs.ammount =orders.ammount -fs.petteyCash
             
             fs.petteyCash =fs.petteyCash +orders.petteyCash
             fs.reporttype='FUND TRANSFER'
             
              
             fs.save()
             return HttpResponseRedirect("/expense")
         
         form2 = dailyreportt(request.POST or None, request.FILES or None)

         if request.method=='POST' and 'btnform2' in request.POST:
           if form2.is_valid() :
           
             fs1 = form2.save(commit=False)
             fs1.billexpense = fs1.petteyCash
             fs1.ammount =orders.ammount -fs1.petteyCash
             fs1.petteyCash =orders.petteyCash
             fs1.reporttype='CORPORATE'
             fs1.save()
            
             return HttpResponseRedirect("/expense")

         form3 = dailyreportt(request.POST or None, request.FILES or None)

         if request.method=='POST' and 'btnform3' in request.POST:
            if form3.is_valid() :
           
             fs1 = form2.save(commit=False)
             fs1.billexpense = fs1.petteyCash
             fs1.ammount =orders.ammount -fs1.petteyCash
             fs1.petteyCash =orders.petteyCash
             fs1.reporttype='COMMISSION'
             fs1.save()
            
             return HttpResponseRedirect("/expense")   
            
         if request.method=='POST' and 'btnform4' in request.POST:
            if form3.is_valid() :
           
             fs1 = form2.save(commit=False)
             fs1.billexpense = fs1.petteyCash
             fs1.ammount =orders.ammount -fs1.petteyCash
             fs1.petteyCash =orders.petteyCash
             fs1.reporttype='Discount'
             fs1.save()
            
             return HttpResponseRedirect("/expense")    

              

               
         products =  paybillcatogory.objects.all()
   
    
         myFilter = expensefilter(request.GET, queryset=products)
         products = myFilter.qs    
        
         context = {#'category': category,
               'orders': orders,
               'form':form,
               'pro':products,
               'user_products':user_products,
               'total':total,
               'form2':form2,
               'form3':form3
               }


         return render(request, 'core/expense.html',context)

def expensestore(request):

         orders=dailyreport.objects.all().last()
         #myFilter =dailyreportfilter(request.GET,queryset=orders)
         user_products = temppaybill.objects.filter(user=request.user)
         
         total=0
         total1=0
         for gs in user_products:
           total+=gs.ammount 

         

         for rs in  user_products:
                detail = paybill()
                detail.paybillcatogory =rs.paybillcatogory
                paybilllast=paybill.objects.all().last()
                 # Order Id
                detail.pettycashbalance=paybilllast.pettycashbalance-rs.ammount
                detail.ammount  = rs.ammount 
                detail.remarks    = rs.remarks
                detail.user  = request.user
                detail.typecat="payment"
                detail.save()
                
                user_products.delete()

         item, created =dailyreport.objects.get_or_create(
            
            petteyCash=orders.petteyCash-total,
            billexpense=total,
            ammount=orders.ammount,
            reporttype="office expense"
            )      
                 

         return HttpResponseRedirect("/expense")



def delete_item(request,id):
        item = UserItem.objects.get(id=id)
        #item1 = sold.objects.get(pk=product_pk)
        item.delete()         
        return HttpResponseRedirect(reverse('cart'))

def delete_itemgroup(request,id):
        item = UserItem.objects.filter(product_id=id)
        #item1 = sold.objects.get(pk=product_pk)
        
        
        item.delete()      
        return HttpResponseRedirect("group")   
         

class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Product.objects.none()

        qs = Product.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs        

def sms(request):
       
 
   account_sid = 'ACd9cb2c9b4c4aaea3a152dae6c8e5ecf7' 
   auth_token = '5f2ae880b9f8f7e3e563adf63ecf978e' 
   client = Client(account_sid, auth_token) 

   products = Product.objects.all()

   totalbalnce=0
   for p in products:
        totalbalnce +=p.price * p.quantity

   mo = Product.objects.filter(mother=True)

   bl=0
   for p in mo:
        bl +=p.price * p.quantity    
   totalbalnce=totalbalnce-bl
   a="total cash"+str(totalbalnce)
   
 
   message = client.messages.create(  
      body=a   , from_='+19386669052',

                              to='+8801624462494' 
                          ) 
 
  
   return HttpResponseRedirect("/")       



def salesreport(request):
   
         orders=dailyreport.objects.all().order_by('id')
         myFilter =dailyreportfilter(request.GET, queryset=orders)
         orders = myFilter.qs
         s=0
         c=0
         e=0
         profit=0
         l=0
         open=0
        
         cash=0
         dew=0
         open2=0
         corporrateex=0
         discount=0
         billa=bill.objects.all()
         closeblance=0
         comm=0
         returnprice=0
         soldlist=sold.objects.all().filter(groupproduct =False)
         orderlist=Order.objects.all()
         officeexpense=0
         pettycashtransfer = 0
         for rs in orders :
            
            # if l==0:
            #   open=rs.ammount
            #   l=l+1
            
            if rs.reporttype == 'office expense':
               officeexpense=rs.billexpense+officeexpense
            returnprice=returnprice+rs.returnprice
            corporrateex=rs.billexpense+ corporrateex
            if rs.reporttype == "COMMISSION":
               comm=comm+rs.billexpense  
            if rs.reporttype == "Discount":     
               discount=rs.billexpense +discount     

            if rs.reporttype == "FUND TRANSFER":     
               pettycashtransfer=rs.billexpense +pettycashtransfer     

            for b in soldlist: 
              if b.order_id == rs.order_id and rs.order_id  is not None:
                 s=b.total_price+s
                 c=b.total_costprice+c
                 e=b.exchange_ammount+e
                 profit=profit+b.totalprofit

            for  t in orderlist:      
               if t.id == rs.order_id and rs.order_id  is not None:
                  cash=t.paid+cash
                  
            for  ac in billa:      
               if ac.order_id == rs.order_id and rs.order_id  is not None:
                  dew=ac.ammount+dew    

         
         #soldlist=sold.objects.filter(order_id__in=s)
         
         
         paginator = Paginator(orders, 15) # Show 25 contacts per page.

         page_number = request.GET.get('page')
         orders = paginator.get_page(page_number)
         

         for x in list(reversed(list(orders)))[0:1]:
            closeblance=x.ammount
        
         if open is not None and  cash is not None and  dew is not None:
           open2= open +dew+cash
         withoutex=s-e
         aftercommmision=closeblance+corporrateex
         totalcost=comm+discount+c+returnprice
         grossprofit=s-totalcost
         netprofit=grossprofit- officeexpense
         percentageprofit=(grossprofit/c ) *100
         duesales=withoutex-cash
         pettycashreportbalnce=closeblance+corporrateex
         commisiondisreportbalnce=pettycashreportbalnce+pettycashtransfer
         cashreturnbalance=commisiondisreportbalnce+comm+discount
         collentionbalance= cashreturnbalance+returnprice
         openbalance=collentionbalance-(cash+dew)
         context = {#'category': category,
               'pettycashreportbalnce':pettycashreportbalnce,
               'commisiondisreportbalnce':commisiondisreportbalnce,
               'cashreturnbalance':cashreturnbalance,
               'collentionbalance':collentionbalance,
               'openbalance':openbalance,
               'orders': orders,
               'myFilter':myFilter,
               'a':soldlist,
               'duesales':duesales,
                'c':c,
                's':s,
                'e':e,
                'pettycashtransfer':pettycashtransfer,
                'percentageprofit':percentageprofit,
                'grossprofit': grossprofit,
                'netprofit':netprofit,
                'totalcost':totalcost,
                'withoutex':withoutex,
                'profit':profit,
                'open':open,
                'cash':cash,
                'dew' :dew,
                'open2':open2,
                'comm' :comm,
                'discount':discount , 
                'closeblance':closeblance,
                'corporrateex':corporrateex,
                'aftercommmision':aftercommmision,
                'returnprice':returnprice,
                'officeexpense':officeexpense,
               }  
    
         return render(request, "core/salesreport.html",context )           


def expensereport(request):

         orders=paybill.objects.all().order_by('id')
         myFilter =paybillfilter(request.GET, queryset=orders)
         orders = myFilter.qs 
       

        
         context = {#'category': category,
               'orders': orders,
               'myFilter':myFilter
               }


         return render(request, 'core/expensereport.html',context)

        


         