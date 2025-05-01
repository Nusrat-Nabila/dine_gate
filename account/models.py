from django.db import models

# Create your models here.
class CustomerUser(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=100,blank=True,null=True)
    user_contect_number=models.IntegerField(blank=True,null=True)
    user_address=models.CharField(max_length=200,blank=True,null=True)
    user_image=models.ImageField(blank=True,null=True)
    user_password=models.CharField(max_length=200,blank=True,null=True)
    role = models.CharField(max_length=20, default='customer')

    def __str__(self):
       return self.user_name



