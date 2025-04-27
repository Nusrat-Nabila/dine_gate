from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=200)
    min_price=models.IntegerField(blank=True,null=True)
    max_price=models.IntegerField(blank=True,null=True)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=100,blank=True,null=True)
    contact_no=models.IntegerField(blank=True,null=True)
    business_reg_id=models.IntegerField()
    password = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    restaurant_name=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=100,blank=True,null=True)
    price=models.IntegerField()

    def __str__(self):
        return (f"Restau_name: {self.restaurant_name} ,item: {self.item_name}")



class Dine_type(models.Model):
    Restuarant_name=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dine_type=models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return (f"Restau_name: {self.Restuarant_name} ,dine: {self.dine_type}")
