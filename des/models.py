
from datetime import date
from setuptools.command.upload import upload
import email
from random import choice, choices
from tkinter import CASCADE
from django.utils import timezone
from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User

# Create your models here.
class categorie(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class subcategorie(models.Model):
    name=models.CharField(max_length=200)

    categories=models.ForeignKey(categorie,on_delete=models.CASCADE)

    def __str__(self):
        return self.name    

class brand(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class color(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class filter_price(models.Model):
    FILTER_PRICE=[
        ('Under 1000','Under 1000'),
        ('1000 to 10000','1000 to 10000'),
        ('10000 to 20000','10000 to 20000'),
        ('20000 to 30000','20000 to 30000'),
        ('30000 to 40000','30000 to 40000'),
        ('40000 to 50000','40000 to 50000'),
        ('50000 to 60000','50000 to 60000'),
        ('60000 to 70000','60000 to 70000'),
        ('70000 to 80000','70000 to 80000'),
        ('80000 to 90000','80000 to 90000'),
        ('90000 to 100000','90000 to 100000'),
        ('100000 to 150000','100000 to 150000'),
    ]
    price=models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price

class product(models.Model):
    CONDITION=('new','new'),('old','old'),
    STOCK=('IN STOCK','IN STOCK'),('OUT STOCK','OUT STOCK'),
    STATUS=('PUBLISH','PUBLISH'),('DRAFT','DRAFT')

    unique_id=models.CharField(unique=True,max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='product_images/img')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    Condition=models.CharField(choices=CONDITION,max_length=100)
    information=models.TextField(null=True)
    description=models.TextField(null=True)
    stock=models.CharField(choices= STOCK,max_length=200)
    status=models.CharField(choices= STATUS,max_length=200)
    created_date=models.DateTimeField(default=timezone.now)

    categories=models.ForeignKey(categorie,on_delete=models.CASCADE)
    brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    color=models.ForeignKey(color,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(filter_price,on_delete=models.CASCADE,default=None)
    
    def save(self,*args,**kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Images(models.Model):
    image=models.ImageField(upload_to='product_image/img')
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class contactus(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    country =models.CharField(max_length=100)
    address =models.TextField()
    city =models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    postalcode =models.IntegerField()
    phone =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    amount =models.CharField(max_length=50)
    Paymentid =models.CharField(max_length=200,null=True,blank=True)
    Paid =models.BooleanField(default=False,null=True)
    date =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    order =models.ForeignKey(Order,on_delete=models.CASCADE)
    products =models.CharField(max_length=200)
    image =models.ImageField(upload_to='product_images/Order_img')
    quantity=models.CharField(max_length=20)
    price =models.CharField(max_length=50)
    total=models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='processing')

    def update_status(self, new_status):
        
        self.status = new_status
        self.save()

    def __str__(self):
        return self.order.user.username

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    image = models.ImageField(default = "default.jpg", upload_to = "profile_pic")

    def __str__(self):
        return f'{self.user.username} Profile'