from django.db import models

# Create your models here.

from  django.contrib.auth.models import User
from restaurant.models import Restaurant
# Create your models here.
class Table_list(models.Model):
    restaurant_name=models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    table_no=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True,auto_now=False)
    start_time=models.IntegerField
    end_time=models.IntegerField

class TableReservation(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    restaurant_name=models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    reserve_date=models.DateTimeField(auto_now_add=True,auto_now=False)
    start_time=models.IntegerField
    end_time=models.IntegerField
    status_choice=(
        ('confirm','confirm'),
        ('cancel','cancel'),
    )
    satus=models.CharField(max_length=100,choices=status_choice)
