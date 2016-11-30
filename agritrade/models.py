from django.db import models
from django.contrib.auth import models as Auth
Season_choices = (('SNY','Sunny'),('WTR','Winter'),('RNY','Rainy'),('SPR','Spring'),)
Soil_health = (('1','Excellent'),('2','Very Good'),('3','Good'),('4','Satisfactory'),('5','Bad'),)

class Customer(models.Model):
    customer_id = models.CharField(verbose_name = "Customer Id",primary_key = True,max_length = 20)
    customer_name = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 20)
    pincode = models.IntegerField()
    Email = models.EmailField()
    gender = models.CharField(choices 
    = (('M','Male'),('F','Female')),max_length = 50,default = None)
    phone = models.IntegerField(default = None,verbose_name="Contact No")
    dob = models.DateField(null = True,blank = True,verbose_name="Date Of Birth")
    class Meta:
        verbose_name = "Register New Customer"
        verbose_name_plural = "Registerd Customers Details "
    def __str__(self):
        return str(self.customer_name)
        
class Crop(models.Model):
    crop_id = models.CharField(primary_key = True,max_length = 20)
    photograph = models.ImageField(upload_to = "C:\DBMS",null = True)
    crop_desc = models.TextField(max_length = 500)
    crop_name = models.CharField(max_length = 50)
    seed = models.CharField(max_length = 50)
    Season = models.CharField(max_length = 50,choices = Season_choices)
    price = models.IntegerField(default = None)
    fertilizer = models.CharField(max_length = 50)
    pesticides = models.CharField(max_length = 50)
    Irrigation = models.BooleanField(verbose_name = "Irrigation")
    Soil_health = models.CharField(max_length = 50,choices = Soil_health)
    Precaution = models.CharField(max_length = 50,default = "A default Precaution")
    
    class Meta:
        verbose_name = "Crop"
        verbose_name_plural = "Crop Details"    
    
    def __str__(self):
        return str(self.crop_name)


class Farmer(models.Model):
    Farmer_Name = models.CharField(max_length = 50)
    farmer_id = models.CharField(primary_key = True,max_length = 20)
    city = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 100)
    state = models.CharField(max_length = 50)
    Email = models.EmailField()
    pincode = models.IntegerField()
    gender = models.CharField(choices = (('M','Male'),('F','Female')),max_length = 50,default = None)
    phone = models.IntegerField(default = None)
    dob = models.DateField(null = True,blank = True)
    def __str__(self):
        return str(self.Farmer_Name)
    class Meta:
        verbose_name = "Register Farmer"
        verbose_name_plural = "Registered Farmer Details"
class Crop_order(models.Model):
    order_id = models.CharField(max_length = 50)
    order_ammount = models.IntegerField()
    customer_id = models.ForeignKey(Customer,on_delete = models.CASCADE)
    crop_for_sale = models.ManyToManyField(Crop)
    quantity = models.IntegerField()
    status = models.CharField(max_length = 200,
                              choices = (('A','Available'),('NA',"Not Available"),)
    )
    order_date = models.DateField()
    farmer_id = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    desc = models.TextField(max_length = 500)
    class Meta:
        verbose_name = "New Crop Order"
        verbose_name_plural = "Customer Order Details"
    def __str__(self):
        
        return str(self.order_id)

class Staff(models.Model):
    staff_id = models.CharField(primary_key = True,max_length = 20)
    staff_name = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 20)
    gender = models.CharField(choices = (('M','Male'),('F','Female')),max_length = 50,default = None)
    pincode = models.IntegerField()
    Email = models.EmailField()
    doj = models.DateField(name = "Date of Joining",auto_now = True);
    dob = models.DateField(auto_now = False)
    staff_type = models.CharField(max_length = 200,
                                  choices = (('1','Admin'),('2','Agricultural Officer'),('3','Agent'),))
    Access_level = models.IntegerField(choices = ((1,'Level 1'),(2,'Level 2'),(3,'Level 3')))
    phone = models.IntegerField(default = None)
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff Details"    
    def __str__(self):
        return str(self.staff_name)
class Store(models.Model):
    store_id = models.IntegerField(primary_key = True)
    Quantity_In = models.IntegerField()
    Quantity_Out = models.IntegerField()
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    Rent = models.IntegerField()
    farmer_id = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Store Details"
    def __str__(self):
        return str(self.store_id)
class Buyer(models.Model):
    buyer_id = models.OneToOneField(Customer,null = False,primary_key = True,default = 0)
    farmer_id = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    gender = models.CharField(choices = (('M','Male'),('F','Female')),max_length = 50,default = None)
    country = models.CharField(max_length = 10)
    phone = models.IntegerField()
    Email = models.EmailField()
    dob = models.DateField(null = True,blank = True)
    def __str__(self):
        return str(self.Email)
    class Meta:
        verbose_name = "Only Buyers"
        verbose_name_plural = "Only Buyers"
        
    
class Comments(models.Model):
    comment_id = models.AutoField(primary_key = True)
    comment = models.TextField(max_length = 450)
    name = models.CharField(max_length = 25,default = None)
    User_id = models.CharField(max_length=30,default = None)
    def __str__(self):
        return str(self.comment_id)
    class Meta:
        verbose_name = "New Comment"
        verbose_name_plural = "All Comments"
class Registration(models.Model):
    Reg_id = models.AutoField(primary_key = True)
    farmer_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Reg_id)
    class Meta:
        verbose_name = "New Registrations"
        verbose_name_plural = "Registered Users"
class Order_Process(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default = None)
    Balance = models.IntegerField(default =None)
    Total = models.IntegerField(default = None)
    Order_id = models.ManyToManyField(Crop_order)
    def __str__(self):
        return str(self.staff_id)
    class Meta:
        verbose_name = "Order Process" 
        verbose_name_plural = "Order Reports"
class Crop_Supply(models.Model):
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    farmer_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    Date = models.DateField()
    Crop_supply_id = models.IntegerField(default = None)
    def __str__(self):
        return str(self.Crop_supply_id)
    class Meta:
        verbose_name = "Crop Supply" 
        verbose_name_plural ="Crop Supplies" 
class Farmer_Plantation(models.Model):
    farmer_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    crop_id = models.ForeignKey(Crop,on_delete = models.CASCADE)
    plantation_id = models.IntegerField(primary_key = True)
    def __str__(self):
        return str(self.plantation_id)
    class Meta:
        verbose_name = "Farmer Plantation" 
        verbose_name_plural = "Farmer Plantations"

class Season_Crop(models.Model):
    crop_id = models.ForeignKey(Crop,on_delete=models.CASCADE)
    Season = models.CharField(max_length = 50,choices = Season_choices)
    Unique_id = models.AutoField(primary_key = True)
    def __str__(self):
        return str(self.Unique_id)
    class Meta:
        verbose_name = "Additional Info to Crop"
        verbose_name_plural = "Crops Based on Seasons"
class Store_Crop(models.Model):
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    crop_id = models.ForeignKey(Crop,on_delete =models.CASCADE)
    uid = models.AutoField(primary_key = True)
    def __str__(self):
        return str(self.uid)
    class Meta:
        verbose_name = "Crop to Store"
        verbose_name_plural = "Available Crops in Stores"
class crop_Quantity_left(models.Model):
    crop_id = models.ForeignKey(Crop,on_delete = models.CASCADE)
    Remaining = models.IntegerField()
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.crop_id)
    class Meta:
        verbose_name = "Update Stock"
        verbose_name_plural = "Quantity left per Crop"
class Farmer_Phones(models.Model):
    id = models.ForeignKey(Farmer,on_delete = models.CASCADE)
    phone_id = models.AutoField(primary_key=True,default = None)
    phone = models.BigIntegerField(default = None)
    def __str__(self):
        return str(self.phone_id)
    class Meta:
        verbose_name = "Farmer Detail"
        verbose_name_plural = "Farmer Contact Details"
class Buyer_Phones(models.Model):
    id = models.ForeignKey(Buyer,on_delete = models.CASCADE)
    phone_id = models.AutoField(primary_key=True,default = None)
    phone = models.BigIntegerField(default = None)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Buyer Contacts"
        verbose_name_plural = "Buyer Contact Details"
class Staff_Phones(models.Model):
    id = models.ForeignKey(Staff,on_delete = models.CASCADE)
    phone_id = models.AutoField(primary_key=True,default = None)
    phone = models.BigIntegerField(default = None)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Staff Contacts" 
        verbose_name_plural = "Staff Contact Details"

class Customer_Phones(models.Model):
    id = models.ForeignKey(Customer,on_delete = models.CASCADE)
    phone_id = models.AutoField(primary_key=True,default = None)
    phone = models.BigIntegerField(default = None)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Customer Contacts" 
        verbose_name_plural = "Customer Contact Details"




from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth,t,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            date_of_birth=date_of_birth,
            type_of = t
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,t ,username, date_of_birth,password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        u = self.create_user(username,
                        password=password,
                        date_of_birth=date_of_birth,
                        type_of = t,
                    )
        u.is_admin = True
        u.save(using=self._db)
        return u


class MyUser(AbstractBaseUser):
    email = models.EmailField(
                        verbose_name='email address',
                        max_length=255,
                        unique=True,
                    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    type_of = models.CharField(choices = (('Farmer','Farmer'),('Buyer','Buyer'),('Staff','Staff'),('Officer','Offiicer'),),max_length = 20)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information"

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    # Create your models here.
