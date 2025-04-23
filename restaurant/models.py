from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=200)
    min_price=models.IntegerField()
    max_price=models.IntegerField()
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    contact_no=models.IntegerField(blank=True,null=True)
    business_reg_id=models.IntegerField()


class Menu(models.Model):
    restaurant_name=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=100)
    price=models.IntegerField()


class Dine_type(models.Model):
    Restuarant_name=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dine_type=models.CharField(max_length=150)
