from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

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
   
    sellprice = models.PositiveIntegerField(default=0,null=True)
    groupname= models.CharField(max_length=200,null=True)
    quantity = models.PositiveIntegerField(default=0,null=True)
    def __str__(self):
        return self.name


       
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200)
       
    def __str__(self):
        return self.name        

class UserItem(models.Model):
    PRODUCT = (
			('Direct', 'Direct'),
			('Exchange', 'Exchange'),
			)
    PRODUCT1 = (
			('Local', 'Local'),
			('Container', 'Container'),
			)        
    engine = (
			('complete', 'complete'),
			('incomplete', 'incomplete'),
			)          
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0,null=True)
    added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    model_no = models.CharField(max_length=200,blank=True,null=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    status=models.CharField(max_length=10,choices=PRODUCT,default='Direct',null=True)
    productype=models.CharField(max_length=10,choices=PRODUCT1,default='Local',null=True)
    enginecomplete=models.CharField(max_length=10,choices=engine,default='complete',null=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True)
    exchange_engine = models.CharField(max_length=500,blank=True,default='')
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
    @property
    def price(self):
        return (self.product.price)

    @property
    def total_price(self):
        return (self.quantity * self.price1)

    def __str__(self):
        return self.product.name




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)
    UserItem  = models.ManyToManyField(UserItem,blank=True)
    left = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True
    )
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    @property
    def total_price(self):
        return (self.quantity * self.product.price)


class sold(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    left = models.PositiveIntegerField(default=0,null=True)
    
    
    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name   