from django import forms  
from core.models import Order, UserItem,Product,mrentry,returnn,sold,bill,dailyreport,temppaybill,mrentryrecord,corportepay
  
class useritem(forms.ModelForm):  
    class Meta:  
        model = Order 
        fields = ['customer','name','address','paid',"discount","Phone",'vehicleno']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
           
        }


class mrr(forms.ModelForm):  
    class Meta:  
        model = mrentry 
        fields = ['supplier','name','address','paid',"discount"]
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
           
          "productype","quantity","engine_no","status","enginecomplete","price1","price2","exchange_ammount","remarks","sparename"
        ]


class returnnform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = returnn
 
        # specify fields to be used
        fields = [
           
          "quantity","returnreason","status","cashreturnprice","duereturnprice" ,
        ]

        

class soldformm(forms.ModelForm):
    class Meta:
        model = sold
        fields = '__all__'
        exclude = ['product','order','user','Phone','customer','discount']



        def clean(self):
            cleaned_data = super().clean()
            quantity = cleaned_data.get('quantity')
            returnquantity = cleaned_data.get('returnquantity')

            if returnquantity and returnquantity > quantity:
                raise forms.ValidationError("Return quantity cannot be greater than so")




class mreditformm(forms.ModelForm):
    class Meta:
        model = mrentryrecord
        fields = '__all__'
        exclude = ['product','order','user','Phone','supplier','discount']

         




class billfrom(forms.ModelForm):
    class Meta:
        model = bill
        fields = ['name', 'ammount', 'billinvoiceid']
        widgets = {
            'name': forms.TextInput(attrs={'size': 20}),  # Adjust the size as needed
            'ammount': forms.NumberInput(attrs={'size': 10}),  # Adjust the size as needed
            'billinvoiceid': forms.TextInput(attrs={'size': 15}),  # Adjust the size as needed
        }




class dailyreportt(forms.ModelForm):  
    class Meta:  
        model =dailyreport
        fields = ['petteyCash','remarks'] 
        labels = {
          "petteyCash": ""
    }
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 2, 'cols': 15}),  # Adjust rows and cols as needed
        }


class tempbilformm(forms.ModelForm):  
    class Meta:  
        model =temppaybill
        fields = ['ammount','remarks']                  
  


class CorportepayForm(forms.ModelForm):
    class Meta:
        model = corportepay
        fields = ['ammount', 'suppiler',  'corpocatagory','remarks']


        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 2, 'cols': 15}),  # Adjust rows and cols as needed
        }
        # You can customize the widgets or add more options if needed