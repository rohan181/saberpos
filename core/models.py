from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
import datetime
from django.db.models import F, Sum
class Product(models.Model):
    CATEGORY = (
			('uttara', 'uttara'),
			('badda', 'badda'),
			)

    PRODUCT = (
			('exchange', 'exchange'),
			('public', 'public'),
			)          
    #shopname = models.CharField(max_length=200, null=True, choices=CATEGORY)        
    name = models.TextField(max_length=200,null=True)
    productcatagory= models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=10,choices=PRODUCT,default='public',null=True)
    added = models.DateTimeField(auto_now_add=True,null=True)
    brand= models.CharField(max_length=200,null=True)
    price = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   
    
    groupname= models.CharField(max_length=200,null=True)
    quantity = models.PositiveIntegerField(default=0,null=True)
    mother = models.BooleanField(null=True,blank=True)
    subpartquantity = models.PositiveIntegerField(default=0,null=True)
    subpartquantity1 = models.PositiveIntegerField(default=0,null=True)
    def __str__(self):
        return self.name


       
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200)
    balance = models.PositiveIntegerField(default=0,null=True)
    
       
    def __str__(self):
        return self.name +" "+str(self.id)

    #class Meta:
      #  ordering = ('name',)           

class UserItem(models.Model):
    PRODUCT = (
			('Direct', 'Direct'),
			('Exchange', 'Exchange'),
			)
    PRODUCT1 = (
			('LocalContainer', ' LocalContainer'),
			('publicContainer', 'publicContainer'),
			)        
    engine = (
			
			('incomplete', 'incomplete'),
            ('complete', 'complete'),
			)

    credit = (('noncredit', 'noncredit'),
			('credit', 'credit'),
			
			)                  
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,related_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0,null=True)
    price1 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    price2 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
    )
    added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    model_no = models.CharField(max_length=200,blank=True,null=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    status=models.CharField(max_length=10,choices=PRODUCT,default='Direct',null=True)
    credit=models.CharField(max_length=10,choices=credit,default='noncredit',null=True)
    productype=models.CharField(max_length=100,choices=PRODUCT1,default='LocalContainer',null=True)
    enginecomplete=models.CharField(max_length=10,choices=engine,default='incomplete',null=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True,blank=True)
    #exchange_engine = models.CharField(max_length=500,blank=True,default='')
    sparename = models.CharField(max_length=200,null=True,blank=True)
    groupproduct = models.BooleanField(null=True,blank=True)
   
    @property
    def price(self):
        return (self.product.price)

    @property
    def total_price(self):
        return (self.quantity * self.price1)

    




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)
    UserItem  = models.ManyToManyField(UserItem,blank=True)
    left = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
        blank=True
    )
    added = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    invoicenumber = models.CharField(max_length=300,null=True,blank=True)
    address = models.CharField(max_length=800,null=True,blank=True)
    vehicleno  = models.CharField(max_length=800,null=True,blank=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice1 = models.PositiveIntegerField(default=0,null=True,blank=True)
    due = models.PositiveIntegerField(default=0,null=True,blank=True)
    @property
    def total_price(self):
        return (self.quantity * self.UserItem.price1)
    

    
    

    

    


class sold(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True)
    costprice = models.PositiveIntegerField(default=0,null=True)
    left = models.PositiveIntegerField(default=0,null=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    
    price1 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    price2 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True,
        blank= True
    )
    name = models.CharField(max_length=200,null=True,blank=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    sparename = models.CharField(max_length=200,null=True,blank=True)
    groupproduct = models.BooleanField(null=True,blank=True)
    @property
    def total_price(self):
        return self.quantity * self.price1 +self.exchange_ammount

    @property
    def profit(self):
        return (self.total_price-self.costprice ) /self.costprice  
    @property
    def profit1(self):
        return self.profit*100   
    @property  
    def totalprofit(self):
        return self.total_price-self.costprice     
    @property
    def total_price1(self):
        return self.quantity * self.price1   
    @property     
    def total_costprice(self):
        return self.quantity * self.costprice     

    def __str__(self):
        return self.product.name 


    @property
    def invoice(self):
        return (self.id+" " +" "+ self.added+"")   



class supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200)
    balance = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
        blank=True
    )
       
    def __str__(self):
        return self.name         



class mrentry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier= models.ForeignKey(supplier, on_delete=models.CASCADE,blank=True,null=True)
  
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)
    UserItem  = models.ManyToManyField(UserItem,blank=True)
    left = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
        blank=True
    )
    added = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=800,null=True,blank=True)
    vehicleno  = models.CharField(max_length=800,null=True,blank=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice1 = models.PositiveIntegerField(default=0,null=True,blank=True)
    due = models.PositiveIntegerField(default=0,null=True,blank=True)
    @property
    def total_price(self):
        return (self.quantity * self.UserItem.price1)
           





class mrentryrecord(models.Model):
   


    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mrentry = models.ForeignKey(mrentry, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True)
    costprice = models.PositiveIntegerField(default=0,null=True)
    left = models.PositiveIntegerField(default=0,null=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    
    price1 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    price2 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    name = models.CharField(max_length=200,null=True,blank=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    sparename = models.CharField(max_length=200,null=True,blank=True)
    groupproduct = models.BooleanField(null=True,blank=True)
    @property
    def total_price(self):
        return self.quantity * self.price1 +self.exchange_ammount

    @property
    def profit(self):
        return (self.total_price-self.costprice ) /self.costprice  
    @property
    def profit1(self):
        return self.profit*100   
    @property  
    def totalprofit(self):
        return self.total_price-self.costprice     
    @property
    def total_price1(self):
        return self.quantity * self.price1   
    @property     
    def total_costprice(self):
        return self.quantity * self.costprice     

    def __str__(self):
        return self.product.name 



class returnn(models.Model):        
     sold = models.ForeignKey(sold, on_delete=models.CASCADE,null=True,blank=True)
     quantity = models.PositiveIntegerField(default=1)
     returnreason = models.CharField(max_length=300,null=True,default='',blank=True)
     
     added = models.DateTimeField(auto_now_add=True,null=True,blank=True)



class bill(models.Model):  
     order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)      
     name = models.TextField(max_length=100,null=True)
     ammount = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
     added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)


class paybillcatogory(models.Model):    
   name = models.TextField(max_length=100,null=True)

   def __str__(self):
        return self.name


class temppaybill(models.Model):    
   paybillcatogory = models.ForeignKey(paybillcatogory, on_delete=models.CASCADE,null=True,blank=True) 
   user = models.ForeignKey(User, on_delete=models.CASCADE)  
   ammount = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   remarks = models.CharField(max_length=800,null=True,blank=True)



class paybill(models.Model):    
   paybillcatogory = models.ForeignKey(paybillcatogory, on_delete=models.CASCADE,null=True,blank=True)   
   ammount = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   pettycashbalance = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   reloadpetteycash = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   typecat=models.CharField(max_length=800,null=True,blank=True)

   user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)   
   remarks = models.CharField(max_length=800,null=True,blank=True)
   added = models.DateTimeField(auto_now_add=True,null=True)



class dailyreport(models.Model):    
   order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)  

   added = models.DateTimeField(auto_now_add=True,null=True) 
   ammount = models.PositiveIntegerField(default=0,null=True)
   petteyCash = models.PositiveIntegerField(default=0,null=True)
   returnn = models.ForeignKey(returnn,on_delete=models.CASCADE,null=True,blank=True)
   bill = models.ForeignKey(bill,on_delete=models.CASCADE,null=True,blank=True)
   returnprice = models.PositiveIntegerField(default=0)
   billexpense = models.PositiveIntegerField(default=0)
   reporttype = models.CharField(max_length=800,null=True,blank=True)

   @property
   def paiddtotal(self):
        return self.order.paid


  
   


class corportepay(models.Model):    
    ammount = models.PositiveIntegerField(default=0)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True,null=True) 
    groupproduct = models.BooleanField(null=True,blank=True)  