from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product
from .filters import OrderFilter

@login_required
def cart(request):
    products = Product.objects.all()
    myFilter = OrderFilter(request.GET, queryset=products)
    products = myFilter.qs 
	
    context = {'products': products,'myFilter':myFilter}
    return render(request, 'core/cart.html', context)