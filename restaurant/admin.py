from django.contrib import admin
from .models import  (Restaurant,Menu,Dine_type)
# Register your models here.
admin.site.register([Restaurant,Menu,Dine_type])
