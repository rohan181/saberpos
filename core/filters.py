from email.policy import default
import django_filters
from django import forms
from django_filters import CharFilter

import django_filters
from django_filters import DateFilter, CharFilter
from dal import autocomplete

from .models import *

from .models import *
import djhacker 


from django.contrib.admin.widgets import AdminDateWidget


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
 
 djhacker.formfield(
    Product.name,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='country-autocomplete')
)
 # added = django_filters.DateFilter(field_name='added', lookup_expr='gte', input_formats=["%m-%d-%Y"])

 class Meta:
      model = Product
      fields = ['name','productcatagory']
      
    
	





class soldfilter(django_filters.FilterSet):
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=AdminDateWidget())
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=AdminDateWidget())
  
  class Meta:
   model = Order
   fields = ['customer']


class dailyreportfilter(django_filters.FilterSet):
  start_date = DateFilter(field_name="added", lookup_expr='gte' ,widget=AdminDateWidget())
  end_date = DateFilter(field_name="added", lookup_expr='lte',widget=AdminDateWidget())
  
  class Meta:
   model = dailyreport
   fields = []   



class expensefilter(django_filters.FilterSet):
  
  
  class Meta:
   model =  paybillcatogory
   fields = ['name'] 

  
    
		

