from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import  update_view,ggroup,group,mrupdate_view,mrproductlist
from . import views

urlpatterns = [
    path(
        'accounts/login/',
        LoginView.as_view(template_name='core/login.html'),
        name='login'
    ),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', views.cart, name='cart'),
    path('mr', views.mr, name='mr'),
    path('<id>/update',update_view ,name='update'),
    path('<id>/mrupdate',mrupdate_view ,name='mrupdate'),
    path('<id>/group',group,name='group'),
    path('soldlist', views.soldlist, name='dataupdate'),
    path('<id>/cashmemo', views.cashmemo, name='cashmemo'),
    path('<id>/returnn', views.returnno, name='return'),
    path('<id>/returnitem', views.returnreasonn, name='returnreasonn'),
    path('<id>/editcashmemo', views.editcashmemo, name='editcashmemo'),
    path('<id>/fianaleditcashmemo', views.fianaleditcashmemo, name='fianaleditcashmemo,'),
    path('productlist', views.productlist, name='productlist'),
    path('mrproductlist', views.mrproductlist, name='mrproductlist'),
]
