from django.contrib import admin
from .models import (Customer,Crop,Buyer_Phones,Farmer,Crop_order,
Staff,Store,Buyer,
Comments,Registration,
Order_Process,
Crop_Supply,Customer_Phones)
from .models import (Farmer_Plantation,
Season_Crop,
Store_Crop,crop_Quantity_left,
Farmer_Phones,
Staff_Phones)
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import MyUser
from django import forms
Models = [Registration,Crop_Supply,Order_Process]
class Staff_Phones_Admin(admin.ModelAdmin):
    list_display = ('staff_id','Staff_Name','phone','city')
    search_fields = ('phone',)

    def Gender(self,obj):
        return str(obj.id.gender)
    def city(self,obj):
        return str(obj.id.city)
    def Staff_Name(self,obj):
        return str(obj.id.staff_name)
    def staff_id(self,obj):
        return str(obj.id.staff_id)

class Customer_Phones_Admin(admin.ModelAdmin):
    list_display = ('customer_id','Customer_Name','phone',)
    def Customer_Name(self,obj):
        return str(obj.id.customer_name)
    def customer_id(self,obj):
        return str(obj.id.customer_id)
admin.site.register(Customer_Phones,Customer_Phones_Admin)
class Farmer_Phones_Admin(admin.ModelAdmin):
    list_display = ('Farmer_id','Farmer_Name','phone',)
    def Farmer_Name(self,obj):
        return str(obj.id.Farmer_Name)
    def Farmer_id(self,obj):
        return str(obj.id.farmer_id)
admin.site.register(Farmer_Phones,Farmer_Phones_Admin)

class Buyer_Phones_Admin(admin.ModelAdmin):
    list_display = ('Buyer_id','Buyer_Name','phone',)
    def Buyer_Name(self,obj):
        return str(obj.id.buyer_id.customer_name)
    def Buyer_id(self,obj):
        return str(obj.id.buyer_id)        
admin.site.register(Buyer_Phones,Buyer_Phones_Admin)
class CustomerAdmin(admin.ModelAdmin):
    #fields = (('customer_name','customer_id'),('Address','city'),('state','pincode'),('Email','gender'),('dob',"phone"),)
    list_display = ("customer_id","customer_name","Address","city","state","phone")
    list_filter = ("gender","dob","city",)
    search_fields = ("customer_name","city","pincode",'phone')

class FarmerAdmin(admin.ModelAdmin):
    fields = (('farmer_id'),('city','Address'),('state','Email',),)
    list_display = ("farmer_id","Farmer_Name","Address","city","state","phone","Email",)
    list_filter = ("gender","dob","city",)
    search_fields = ("Farmer_Name","city","pincode")
    
    
class BuyerAdmin(admin.ModelAdmin):
    search_fields = ("buyer_id",)
    def get_buyer(self,obj):
        print(obj)
        return obj.buyer_id.customer_name
        
    list_display = ("buyer_id",'get_buyer','country','gender','phone','Email','dob')
    list_filter = ("gender","dob",'farmer_id')
    
    get_buyer.short_description = "Name"
class CropAdmin(admin.ModelAdmin):
    list_display = ("crop_id","crop_name","crop_desc","price","seed","Season",)
    list_filter = ("crop_name","price","Season",)
    search_fields = ("crop_name","Season","Irrigation","crop_id",)
    
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ("staff_id","staff_name","Address","city","state","gender","pincode","Email","Date of Joining","staff_type")
    list_filter = ("staff_type","gender","state",)
    search_fields = ("staff_name","city","pincode","staff_id")
class Comment_admin(admin.ModelAdmin):
    list_filter = ("name","comment_id",)
    list_display = ("comment_id","name","comment",)
    pass
class Crop_Order_Admin(admin.ModelAdmin):
    def crops(self,obj):
        Cr = obj.crop_for_sale
        crops = [cr.crop_name for cr in Cr.all()]
        final = ' '.join(crops)
        return str(final)
    list_display = ('customer_id','order_id','crops','order_ammount',"quantity","status","order_date")
    list_filter = ('order_date','customer_id',)
    


class Store_crop_Admin(admin.ModelAdmin):
    def get_crop_name(self,obj):
        id2 = obj.crop_id
        Crops = Crop.objects.get(crop_id = id2)
        return str(Crops.crop_name)
    list_display = ("uid","store_id","crop_id","get_crop_name")
    
class Store_Admin(admin.ModelAdmin):
    def Remaining_Stock(self,obj):
        remaing = obj.Quantity_In - obj.Quantity_Out
        return str(remaing)
    def Number_of_crops(self,obj):
        pass
    list_display = ("store_id","Remaining_Stock")

class Farmer_Plantation_Admin(admin.ModelAdmin):
    list_display = ("plantation_id","farmer_id","farmer_name","crop_id",)
    def farmer_name(self,obj):
        return obj.farmer_id.Farmer_Name
class Crop_supply_admin(admin.ModelAdmin):
    list_display = ("store_id","farmer_id","Date","Crop_supply_id")
    list_filter = ('store_id',"farmer_id","Date")
class Season_crop_Admin(admin.ModelAdmin):
    list_display = ("crop_id","Season","Unique_id",)
class Phone_Admin(admin.ModelAdmin):
    def farmer_name(self,obj):
        return obj.id.Farmer_Name
    list_display = ("farmer_name","phone",)
    list_links = ('farmer_name',"phone")
class Store_Crop_Admin(admin.ModelAdmin):

    def Crop_Name(self,obj):
        return obj.crop_id.crop_name
    list_display = ("store_id","Crop_Name",)
    list_filter = ("store_id","crop_id",)
admin.site.register(Season_Crop,Season_crop_Admin)
admin.site.register(Crop_Supply,Crop_supply_admin)
admin.site.register(Farmer_Plantation,Farmer_Plantation_Admin)

admin.site.register(Store_Crop,Store_Crop_Admin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Farmer,FarmerAdmin)
admin.site.register(Buyer,BuyerAdmin)
admin.site.register(Crop,CropAdmin)
admin.site.register(Staff,StaffAdmin)

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('')
admin.site.register(MyUser)
#admin.site.register(Models)
admin.site.register(Comments,Comment_admin)
admin.site.register(Crop_order,Crop_Order_Admin)
admin.site.register(Store,Store_Admin)
admin.site.register(Staff_Phones,Staff_Phones_Admin)

# Register your models here.
