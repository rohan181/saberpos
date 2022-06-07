from django import forms  
from core.models import Order, UserItem 
  
class useritem(forms.ModelForm):  
    class Meta:  
        model = Order 
        fields = ['customer','left']