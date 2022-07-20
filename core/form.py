from django import forms  
from core.models import Order, UserItem,Product
  
class useritem(forms.ModelForm):  
    class Meta:  
        model = Order 
        fields = ['customer','left','name','address','paid']




 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Product
 
        # specify fields to be used
        fields = [
           
            "sellprice",
        ]
