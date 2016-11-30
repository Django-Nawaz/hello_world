from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from .models import Customer,Crop,Buyer_Phones,Farmer,Crop_order,Staff,Store,Buyer,Comments,Registration,Order_Process,Crop_Supply
from .models import Farmer_Plantation,Season_Crop,Store_Crop,crop_Quantity_left,Farmer_Phones,Staff_Phones
from django import forms
from .forms import StaffRegForm,BuyerRegForm,CustomerRegForm,FarmerRegForm,CustLogin,FarmerLogin,StaffLogin,BuyerLogin
from django.contrib.auth import authenticate
from .models import MyUser
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django import views
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
User = get_user_model()
from rest_framework import serializers
def Buyer_Reg(request):
    if request.method == 'POST':
        form = BuyerRegForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usernamed = data['Email']
            passwordd = data['password1']
            try:
                user = authenticate(email = usernamed,password = passwordd)
                user1 = authenticate(username = usernamed,password = passwordd)
            except Exception as E:
                print(E)
            if data['password1']==data['password2'] and user is None:
                del data['password1']
                del data['password2']
                user = MyUser.objects.create_user(email = usernamed,password = passwordd,t = 'Buyer',date_of_birth = data['dob'])
                USER = User.objects.create_user(username = usernamed,password = passwordd,is_staff = True)
                g = Group.objects.get(name = "Buyer_Group")
                g.user_set.add(USER)
                USER.save()
                print(data)
                b = form.save()
                print(b)
                user.save()
                
                #print("Buyer Registered Successfully")
                url = reverse('Buyer_login')
                print(url)
                context = {'url':url,'type':'Buyer'}               
                return render(request,"reg_complete.html",context)
            else:
                print("Password Mismatch")
                return HttpResponse("Password Mismatch")
                
        else:
            print("Invalid Form")
            return HttpResponse("Invalid")
    else:
        form = BuyerRegForm()
        context = {'form':form,
                   'site_title':"Register the Buyer",
                   'site_header':"Agricultral Trading Management System",
                   'header_s':"Enter the form below to Register The Buyer",
                   'site_url':"/",
        }
        return render(request,"registration.html",context)
def Farmer_Reg(request):
    if request.method == 'POST':
        form = FarmerRegForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usernamed = data['Email']
            passwordd = data['password1']
            try:
                user = authenticate(username = usernamed,password = passwordd)
            except Exception as E:
                print(E)
            if data['password1']==data['password2'] and user is None:
                del data['password1']
                del data['password2']
                user = MyUser.objects.create_user(email = usernamed,password = passwordd,t = 'Buyer',date_of_birth = data['dob'])
                USER = User.objects.create_user(username = usernamed,password = passwordd,is_staff = True)
                g = Group.objects.get(name = "Farmer_Group")
                g.user_set.add(USER)
                print(data)
                b = form.save()
                
                print(b)
                user.save()
                
                #print("Farmer Registered Successfully")
                url = reverse('Farmer_login')
                print(url)
                context = {'url':url,'type':'Farmer'}               
                return render(request,"reg_complete.html",context)
            else:
                print("Password Mismatch")
                return HttpResponse("Password Mismatch")
                
        else:
            print("Invalid Form")
            return HttpResponse("Invalid") 
    else:
        form = FarmerRegForm()
        context = {'form':form,
                   'site_title':"Register the Farmer",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter the form below to Register the Farmer",
                   'site_url':"/",
        }
        return render(request,"registration.html",context)
        
def Staff_Reg(request):
    if request.method == 'POST':
        form = StaffRegForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usernamed = data['Email']
            passwordd = data['password1']
            try:
                user = authenticate(username = usernamed,password = passwordd)
            except Exception as E:
                print(E)
            if data['password1']==data['password2'] and user is None:
                #del data['password1']
                #del data['password2']
                
                user = MyUser.objects.create_user(email = usernamed,password = passwordd,t = 'Staff',date_of_birth = data['dob'])
                USER = User.objects.create_user(username = usernamed,password = passwordd,is_staff = True)
                g = Group.objects.get(name = "Staff_Group")
                g.user_set.add(USER)
                print(data)
                b = form.save()
                print(b)
                user.save()
                print("Staff Registered Successfully")
                url = reverse('Staff_login')
                print(url)
                context = {'url':url,'type':'Staff'}               
                return render(request,"reg_complete.html",context)
            else:
                print("Password Mismatch")
                return HttpResponse("Password Mismatch")
                
        else:
            print("Invalid Form")
            return HttpResponse("Invalid")
             
    else:
        form = StaffRegForm()
        context = {'form':form,
                   'site_title':"Register the Staff",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter the form below to Register Staff",
                   'site_url':"/",
        }
        print("Here")
        return render(request,"registration.html",context)
def Customer_Reg(request):
    if request.method == 'POST':
        form = CustomerRegForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usernamed = data['Email']
            passwordd = data['password1']
            try:
                user = authenticate(email = usernamed,password = passwordd)
            except Exception as E:
                print(E)
            if data['password1']==data['password2'] and user is None:
                del data['password1']
                del data['password2']
                print(data)
                user = MyUser.objects.create_user(email = usernamed,password = passwordd,t = 'Customer',date_of_birth = data['dob'])
                USER = User.objects.create_user(username = usernamed,password = passwordd,is_staff = True)
                g = Group.objects.get(name = "Customer_Group")
                g.user_set.add(USER)                
                print(data)
                b = form.save()
                
                print(b)
                user.save()
                print("Farmer Registered Successfully")
                url = reverse('Customer_login')
                print(url)
                context = {'url':url,'type':'Customer'}               
                return render(request,"reg_complete.html",context)
            else:
                print("Password Mismatch")
                return HttpResponse("Password Mismatch")
                
        else:
            print("Invalid Form")
            return HttpResponse("Invalid")
    else:
        form = CustomerRegForm()
        context = {'form':form,
                   'site_title':"Register the Customer",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter the form below to Register the Customer",
                   'site_url':"/",
        }
        return render(request,"registration.html",context)
def Customer_Login(request):
    if request.method == 'POST':
        form = CustLogin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(username = data['Email'],password = data['password'])
            try:
                user1 = MyUser.objects.get(email = data['Email'])
            except:
                return HttpResponse("Login Failure")
            request.session['UserName'] = data['Email']
            if user is not None:
                if user1.type_of == 'Customer': 
                    context = {'people':Customer.objects.all()}
                    return render(request,"login_home.html",context)
                else:
                    return HttpResponse("Only Customer Can Login But you are " + str(user1.type_of))
            else:
                print("Failure")
                return HttpResponse("Login Failure")
        else:
            return HttpResponse("Error")
    else:
        form = CustLogin()
        
        context = {'form':form,
                   'site_title':"Customer Login ",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter Username and Password to Login",
                   'site_url':"/",
                   'type_of':"Customer",
        }
        return render(request,"login.html",context)
def Staff_Login(request):
    if request.method == 'POST':
        form = StaffLogin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(username =data['Email'],password = data['password'])
            user1 = MyUser.objects.get(email = data['Email'])
            print(user1.type_of)
            if user is not None:
                if user1.type_of == 'Staff': 
                    request.session['username'] =  data['Email']
                    context = {'people':Staff.objects.all()}
                    return render(request,"login_home.html",context)
                else:
                    return HttpResponse("Only Customer Can Login But you are " + str(user1.type_of))
            else:
                print("Failure")
                return HttpResponse("Login Failure")
        else:
            return HttpResponse("Error") 
            
    else:
        form = StaffLogin()
        context = {'form':form,
                   'site_title':"Staff Login ",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter Username and Password to Login",
                   'site_url':"/",
                   'type_of':"Staff",
        }
        return render(request,"login.html",context)
        
def Admin_Login(request):
    if request.method == 'POST':
        form = StaffLogin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(username =data['Email'],password = data['password'])
            user1 = MyUser.objects.get(email = data['Email'])
            print(user1.type_of)
            if user is not None:
                if user1.type_of == 'Admin': 
                    request.session['username'] =  data['Email']
                    context = {'people':User.objects.all()}
                    return render(request,"login_home.html",context)
                else:
                    return HttpResponse("Only Admin Can Login But you are " + str(user1.type_of))
            else:
                print("Failure")
                return HttpResponse("Login Failure")
        else:
            return HttpResponse("Error") 
            
    else:
        form = StaffLogin()
        context = {'form':form,
                   'site_title':"Staff Login ",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter Username and Password to Login",
                   'site_url':"/",
                   'type_of':"Staff",
        }
        return render(request,"login.html",context)
        
def Farmer_Login(request):
    if request.method == 'POST':
        form = FarmerLogin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(username =data['Email'],password = data['password'])
            user1 = MyUser.objects.get(email = data['Email'])
            print(user1.type_of)
            if user is not None:
                if user1.type_of == 'Farmer': 
                    return HttpResponse("Login Successfull")
                else:
                    return HttpResponse("Only Farmer Can Login But you are " + str(user1.type_of))
            else:
                print("Failure")
                return HttpResponse("Login Failure")
        else:
            return HttpResponse("Error") 
    else:
        form = FarmerLogin()
        context = {'form':form,
                   'site_title':"Farmer Login ",
                   'site_header':"Agicultral Trading Management System",
                   'header_s':"Enter Username and Password to Login",
                   'site_url':"/",
                   'type_of':"Farmer",
        }
        return render(request,"login.html",context)
def Buyer_Login(request):
    if request.method == 'POST':
        form = BuyerLogin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(username =data['Email'],password = data['password'])
            user1 = MyUser.objects.get(email = data['Email'])
            print(user1.type_of)
            if user is not None:
                if user1.type_of == 'Buyer': 
                    context = {'crops':Crop.objects.all(),'stores':Store.objects.all()}
                    return render(request,"market_place.html",context)
                else:
                    return HttpResponse("Only Buyer Can Login But you are " + str(user1.type_of))
            else:
                print("Failure")
                return HttpResponse("Login Failure")
        else:
            return HttpResponse("Error") 
    else:
        form = BuyerLogin()
        context = {'form':form,
                   'site_title':"Buyer Login ",
                   'site_header':"Agricultral Trading Management System",
                   'header_s':"Enter Username and Password to Login",
                   'site_url':"/",
                   'type_of':"Buyer",
        }
        return render(request,"login.html",context)              
# Create your views here.
