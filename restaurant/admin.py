from django.contrib import admin
from .models import Restaurant, Menu, Dine_type


# Register the models with their custom admin classes
admin.site.register([Restaurant,Menu, Dine_type])