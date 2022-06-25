import django_filters
from django_filters import CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):

 catagory = (
    ('Engine', 'Engine'),
    
    ('Suspention', 'Suspention'),
    ('Gear Box', 'Gear Box'),
    ('Booster', 'Booster'),
    ('Master Salander', 'Master Salander'),
    
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
 #productcatagory =ModelChoiceField(field_name='productcatagory', lookup_expr='icontains')
 productcatagory = django_filters.ChoiceFilter(choices=catagory ,field_name='productcatagory')
 brand = django_filters.ChoiceFilter(choices=brand ,field_name='brand')
 class Meta:
		model = Product
		fields = '__all__'
		exclude = ['price','quantity']