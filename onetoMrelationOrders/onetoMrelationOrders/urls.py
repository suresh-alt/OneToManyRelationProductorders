"""onetomaryrelation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app1 import views
from onetoMrelationOrders import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name='main'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogincheck/',views.adminlogincheck,name='adminlogincheck'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path("customerlogin/",views.customerlogin,name='customerlogin'),
    path('creg/',views.creg,name='creg'),
    path('clogincheck',views.clogincheck,name='clogincheck'),
    path('addp/',views.addp,name='addp'),
    path('savep',views.savep,name='savep'),
    path('vpro/',views.vpro,name='vpro'),
    path('orderp/',views.orderp,name='orderp'),
    path('orders/',views.orders,name='orders'),
    path('corder/',views.corder,name='corder')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)