from django import forms  
from core.models import Order, UserItem,Product,mrentry,returnn,sold,bill
  
class useritem(forms.ModelForm):  
    class Meta:  
        model = Order 
        fields = ['customer','left','name','address','paid',"discount","Phone",'vehicleno']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
           
        }


class mrr(forms.ModelForm):  
    class Meta:  
        model = mrentry 
        fields = ['supplier','left','name','address','paid',"discount"]
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
           
          "productype","quantity","engine_no","status","enginecomplete","price1","price2","exchange_ammount","exchange_engine","remarks",'credit',"sparename"
        ]


class returnnform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = returnn
 
        # specify fields to be used
        fields = [
           
          "quantity","returnreason"
        ]


class soldformm(forms.ModelForm):
    class Meta:
        model = sold
        fields = '__all__'
        exclude = ['product','order','user','Phone','customer','discount']
         




class billfrom(forms.ModelForm):  
    class Meta:  
        model =bill
        fields = ['name','ammount','customer']         