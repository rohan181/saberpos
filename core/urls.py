from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import  update_view,ggroup,group
from . import views

urlpatterns = [
    path(
        'accounts/login/',
        LoginView.as_view(template_name='core/login.html'),
        name='login'
    ),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', views.cart, name='cart'),
    path('<id>/update',update_view ,name='update'),
    path('<id>/group',group,name='group'),
    path('soldlist', views.soldlist, name='dataupdate'),
    path('<id>/cashmemo', views.cashmemo, name='cashmemo'),
]
