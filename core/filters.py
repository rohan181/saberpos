from email.policy import default
import django_filters
from django import forms
from django_filters import CharFilter

import django_filters
from django_filters import DateFilter, CharFilter, DateTimeFilter
from dal import autocomplete

from .models import *

from .models import *



from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget


class OrderFilter(django_filters.FilterSet):

 catagory = (
    ('Engine', 'Engine'),

    ('Suspention', 'Suspention'),
    ('Gear Box', 'Gear Box'),
    ('Booster', 'Booster'),
    ('Master Salander', 'Master Salander'),
    ('Master Cylinder', 'Master Cylinder'),
    ('Nose Cut', 'Nose Cut'),
    ('AC Cooling Box', 'AC Cooling Box'),
    ('Difencel', 'Difencel'),
    ('Others', 'Others'),
    ('Popular Shape', 'Popular Shape'),
    ('Back Light', 'Back Light'),
    ('Tana Door', 'Tana Door'),
    ('Side Door', 'Side Door'),
    ('Back Door', 'Back Door'),
    ('Back Bumper', 'Back Bumper'),
    ('Mudgard', 'Mudgard'),
    ('Bonut', 'Bonut'),
    ('Air Clean Box', 'Air Clean Box'),
    ('Front Door', 'Front Door'),
    ('Rear Bar', 'Rear Bar'),
    ('Stearing Wheel', 'Stearing Wheel'),
    ('Cabin', 'Cabin'),
    ('Half Cut', 'Half Cut'),
    ('Back Suspention', 'Back Suspention'),
    ('Roof Top', 'Roof Top'),
    ('Face Cut', 'Face Cut'),
)

 brand = (
    ('Toyota', 'Toyota'),
    ('Nissan', 'Nissan'),
    ('Honda', 'Honda'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Suzuki', 'Suzuki'),
)

 name = CharFilter(field_name='name', lookup_expr='icontains')
 # productcatagory =ModelChoiceField(field_name='productcatagory', lookup_expr='icontains')
 productcatagory = django_filters.ChoiceFilter(
     choices=catagory, field_name='productcatagory')
 brand = django_filters.ChoiceFilter(choices=brand, field_name='brand')
 
 
 # added = django_filters.DateFilter(field_name='added', lookup_expr='gte', input_formats=["%m-%d-%Y"])

 class Meta:
      model = Product
      fields = ['productcatagory','name']
      
    
	





class soldfilter(django_filters.FilterSet):
  
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=forms.DateInput(attrs={'type': 'date'}),)
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date'}))
  #start_time = DateTimeFilter(field_name="added", lookup_expr='time__gte', widget=AdminTimeWidget())
  #end_time = DateTimeFilter(field_name="added", lookup_expr='time__lte', widget=AdminTimeWidget())
  invoicenumber = CharFilter(field_name='invoicenumber', lookup_expr='icontains')
  class Meta:
   model = Order
   fields = ['customer','invoicenumber']


class mrfilter(django_filters.FilterSet):
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date'}))
  
  class Meta:
   model = mrentry
   fields = ['supplier']

class dailyreportfilter(django_filters.FilterSet):
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date'}))
  
  class Meta:
   model = dailyreport
   fields = []   



class returnfilter(django_filters.FilterSet):
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date'}))
  
  class Meta:
   model = returnn
   fields = []  


class expensefilter(django_filters.FilterSet):
  
  
  class Meta:
   model =  paybillcatogory
   fields = ['name'] 


class paybillfilter(django_filters.FilterSet):
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=forms.DateInput(attrs={'type': 'date'}))
  
  class Meta:
   model = paybill
   fields = []   
  
    
		

