from django.db import models
from account.models import CustomerUser
from restaurant.models import Restaurant
# Create your models here.
class Table_list(models.Model):
    restaurant=models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    table_no=models.CharField(max_length=100,blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    start_time=models.TimeField(blank=True,null=True)
    end_time=models.TimeField(blank=True,null=True)
    no_of_people=models.IntegerField(blank=True,null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('restaurant', 'table_no', 'date', 'start_time', 'end_time')

    def __str__(self):
        return (f"Restau_name: {self.restaurant.restaurant_name} ,item: {self.table_no}")

class TableReservation(models.Model):
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    table=models.ForeignKey(Table_list ,on_delete=models.CASCADE)
    reserve_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    status_choice=(
        ('confirm','confirm'),
        ('cancel','cancel'),
    )
    status=models.CharField(max_length=100,choices=status_choice)

    def __str__(self):
        return (f"user: {self.user.user_name} ,Restau_name: {self.restaurant.restaurant_name}")
