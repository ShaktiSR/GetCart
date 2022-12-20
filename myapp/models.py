from django.db import models
from django.contrib.auth.models import AbstractUser, User
import datetime

from django.db.models.fields import CharField

class ulimiter(models.Model):
    #creating database table (makemigrations means create changes and store in a file)
    #________________________(migrate means apply the pending changes created by makemigrations)
    uid=models.TextField() 
    ulimit=models.IntegerField(default=0)
    
    def __str__(self):
        return self.uid



# Create your models here.
class Contect(models.Model):
    #creating database table (makemigrations means create changes and store in a file)
    #________________________(migrate means apply the pending changes created by makemigrations)
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField() 
    date=models.DateField()

    #to change the view of representation of tables in admin page
    def __str__(self):
        return self.name
class Poll(models.Model):
    loguser =models.CharField(max_length=30, default="admin")
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    def __str__(self):
        return self.question
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count


class Category(models.Model):
    name=models.CharField(max_length=80)
    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=80)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    description=models.CharField(max_length=300, default="")
    tags=models.CharField(max_length=300, default="")
    image=models.ImageField(upload_to="products/")
    def __str__(self):
        return self.name

class order(models.Model):
    ord_prod=models.ForeignKey(product, on_delete=models.CASCADE)
    ord_cust=models.ForeignKey(User, on_delete=models.CASCADE)
    ord_quant=models.IntegerField(default=1)
    ord_price=models.IntegerField()
    address=CharField(max_length=200, default="")
    phone = models.IntegerField(default=0, blank=True)
    ord_date=models.DateField(default=datetime.datetime.today)
    ord_status=models.BooleanField(default=False)

    #payment_status=models.BooleanField(default=False)
    #razorpay_order_id=models.CharField(max_length=500,default="")
    #razorpay_payment_id=models.CharField(max_length=500,default="")
    #razorpay_signature=models.CharField(max_length=500,default="")
    
    def placeorder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(cust_id):
        return order.objects.filter(ord_cust=cust_id).order_by('-ord_date')
    

#class marked(models.Model):
#    has_answered = models.ManyToManyField(User)
#    question_text = models.CharField(max_length=80)