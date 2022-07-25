from django import forms  
from core.models import Order, UserItem,Product
  
class useritem(forms.ModelForm):  
    class Meta:  
        model = Order 
        fields = ['customer','left','name','address','paid',"discount"]




 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = UserItem
 
        # specify fields to be used
        fields = [
           
          "productype","quantity","engine_no","status","enginecomplete","price1","price2","exchange_ammount","exchange_engine","remarks",
        ]
