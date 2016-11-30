# -*- coding: utf-8 -*-
from django import forms
from .models import Customer,Buyer,Farmer,Staff

class StaffRegForm(forms.ModelForm):
    password1 = forms.CharField(widget = forms.PasswordInput,label = "Password")
    password2 = forms.CharField(widget = forms.PasswordInput,label= "Retype Password")
    class Meta:
        model = Staff
        fields = "__all__"
        

class BuyerRegForm(forms.ModelForm):
    password1 = forms.CharField(widget = forms.PasswordInput,label = "Password")
    password2 = forms.CharField(widget = forms.PasswordInput,label= "Retype Password",max_length=10,min_length=6)
    class Meta:
        model = Buyer
        fields ="__all__"
        
class FarmerRegForm(forms.ModelForm):
    password1 = forms.CharField(widget = forms.PasswordInput,label = "Password")
    password2 = forms.CharField(widget = forms.PasswordInput,label= "Retype Password")
    class Meta:
        model = Farmer
        fields = "__all__"

class CustomerRegForm(forms.ModelForm):
    password1 = forms.CharField(widget = forms.PasswordInput,label = "Password")
    password2 = forms.CharField(widget = forms.PasswordInput,label= "Retype Password")
    class Meta:
        model = Customer
        fields = "__all__"

class CustLogin(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ['Email',]
class FarmerLogin(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Farmer
        fields = ['Email',]     
class BuyerLogin(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Buyer
        fields = ['Email',]
class StaffLogin(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Staff
        fields = ['Email',]
class Crop_Purchase(forms.ModelForm):
    crop = forms.CharField(widget = forms.TextInput)
    quantity = forms.FloatField(widget = forms.NumberInput)

        