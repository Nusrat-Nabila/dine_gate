from django.db import models
from django.utils.text import slugify

# Create your models here.
class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=200)
    s_time=models.TimeField(blank=True,null=True)
    e_time=models.TimeField(blank=True,null=True)
    min_price=models.IntegerField(blank=True,null=True)
    max_price=models.IntegerField(blank=True,null=True)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    email=models.EmailField(max_length=100,blank=True,null=True)
    contact_no=models.IntegerField(blank=True,null=True)
    business_reg_id=models.IntegerField()
    password = models.CharField(max_length=128,blank=True,null=True)
    logo=models.ImageField(blank=True,null=True)
    role = models.CharField(max_length=20, default='restaurant')
    slug = models.SlugField(unique=True, blank=True,null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.restaurant_name)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=100,blank=True,null=True)
    price=models.IntegerField()

    def __str__(self):
        return (f"Restau_name: {self.restaurant.restaurant_name} ,item: {self.item_name}")



class Dine_type(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dine_choice=(
        ('Deshi traditional restaurant','Deshi traditional restaurant'),
        ('Biriyani house','Biriyani house'),
        ('cafe lounge','cafe lounge'),
        ('buffet','buffet'),
        ('fine dining','fine dining'),
        ('rooftop dining','rooftop dining'),
        ('seafood restaurant','seafood restaurant'),
        ('fast food & burger joint','fast food & burger joint'),
        ('family dining','family dining'),
    )
    dine_type=models.CharField(max_length=150,choices=dine_choice)

    def __str__(self):
        return (f"Restau_name: {self.restaurant.restaurant_name} ,dine: {self.dine_type}")
