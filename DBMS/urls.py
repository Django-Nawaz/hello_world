"""DBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.site.site_header = "Agricultural Trading Management System"
admin.site.site_title = "DBMS Project"
admin.site.index_title = ""
from agritrade import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin1/', views.Admin_Login,name = 'Admin_Login'),
    url(r'^register/[Bb]uyer/',views.Buyer_Reg,name = 'Buyer_Reg'),
    url(r'^register/[Cc]ustomer/',views.Customer_Reg,name = 'Customer_Reg'),
    url(r'^register/[Ff]armer/',views.Farmer_Reg,name = 'Farmer_Reg'),
    url(r'^register/[Ss]taff/',views.Staff_Reg,name = 'Staff_Reg'),
    url(r'^[lL]ogin/[Cc]ustomer/',views.Customer_Login,name = 'Customer_login'), 
    url(r'^[lL]ogin/[Bb]uyer/',views.Buyer_Login,name = 'Buyer_login'),
    url(r'^[lL]ogin/[Ff]armer/',views.Farmer_Login,name = 'Farmer_login'),
    url(r'^[lL]ogin/[Ss]taff/',views.Staff_Login,name = 'Staff_login'),
]
