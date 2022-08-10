from django import forms  
from core.models import Order, UserItem,Product
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
  
class useritem(forms.ModelForm):  
    invoiceid = forms.DateTimeField(widget=DateTimePicker())
    class Meta:  
        model = Order 
        
        fields = ['customer','left','name','address','paid',"discount","invoiceid"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
           
        }

        



 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = UserItem
 
        # specify fields to be used
        fields = [
           
          "productype","quantity","engine_no","status","enginecomplete","price1","price2","exchange_ammount","exchange_engine","remarks",'credit',
        ]
