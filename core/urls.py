from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include
from .views import  update_view,ggroup,group,mrupdate_view,customersolddeatails,chalan,billcustomer,groupupdate_view,dalyreport,dalyreportsearch,expenseform,expensestore,addproduct,addproductgroup,CountryAutocomplete,sms,salesreport,expensereport,api_productlist,delete_user_item,apiaddproduct,userItemstore,mreditcashmemo

from django.urls import re_path as url
from django.urls import reverse
from . import views

urlpatterns = [
    path(
        'accounts/login/',
        LoginView.as_view(template_name='core/login.html'),
        name='login'
    ),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', views.cart, name='cart'),
    path('salesreport', views.salesreport, name='salesreport'),
    path('mr', views.mr, name='mr'),
    path('corporatepayment', views.corporatepayment, name='corporatepayment'),
  
    path('autocomplete/', views.AutocompleteView.as_view(), name='autocomplete'),
    path('<id>/update',update_view ,name='update'),
    path('<id>/addproduct',addproduct ,name='update'),
    path('<id>/addproductgroup',views.addproductgroup ,name='update'),
    path('<id>/groupupdate',groupupdate_view ,name='update'),
    path('<id>/mrupdate',mrupdate_view ,name='mrupdate'),
    path('<id>/group',group,name='group'),
    path('soldlist', views.soldlist, name='soldlist'),
    path('mrlist', views.mrlist, name='mrlist'),


    path('<id>/cashmemo', views.cashmemo, name='cashmemo'),
    path('<id>/cashmemo1', views.cashmemo1, name='cashmemo1'),
     path('<id>/deleteinvoice', views.deleteinvoice, name='deleteinvoice'),

   # path('<id>/mrmemo', views.mrmemo, name='mrmemo'),
    path('<id>/chalan', views.chalan, name='chalan'),
    path('<id>/returnn', views.returnno, name='return'),
    path('<id>/returnitem', views.returnreasonn, name='returnreasonn'),
    path('returnlist', views.returnlist, name='returnlist'),
    #bill
    path('bill_list', views.bill_list, name='bill_list'),

    path('<id>/editcashmemo', views.editcashmemo, name='editcashmemo'),
    path('<id>/fianaleditcashmemo', views.fianaleditcashmemo, name='fianaleditcashmemo'),
    path('productlist', views.productlist, name='productlist'),


    path('mrinvoicelist', views.mrinvoicelist, name='mrinvoicelist'),
    path('<id>/mrcashmemo', views.mrcashmemo, name='mrcashmemo'),
    path('<id>/mreditcashmemo', views.mreditcashmemo, name='mreditcashmemo'),
    path('<id>/mrfianaleditcashmemo', views.mrfianaleditcashmemo, name='mrfianaleditcashmemo'),

    path('<id>/bill', views.billt, name='bill'),
    path('<id>/delete', views.delete_item, name='delete'),
    path('<id>/deletegroup', views.delete_itemgroup, name='delete'),
    path('<id>/billcustomer', views.billcustomer, name='bill'),

    path('customerlist', views.customerlist, name='customerlist'),
    path('customerdetail', views.customersolddeatails, name='bill'),
    path("search/", views.search, name="search_results"),
    path("daily", views.dalyreport, name=""),
    path("expensereport", views.expensereport, name=""),


    path("expense", views.expense, name=""),
    

    
    path("sms", views.sms, name="sms"),
    path("<id>/expenseform", views.expenseform ,name=""),
    path("expensestore", views.expensestore ,name=""),
   # path("dailysearchresult", views.dalyreportsearch, name="search_results"),
    #path("corporatepay", views.corporatepayment ,name=""),


    #api

    path('api_productlist/', views.api_productlist, name="api_productlist"),
    path('api-delete/<int:item_id>/', views.delete_user_item, name='delete_user_item'),
    path('apiaddproduct/<int:item_id>/', views.apiaddproduct, name='apiaddcart'),

    path('api_useritemstore/', views.userItemstore, name="userItemstore"),
]


   

