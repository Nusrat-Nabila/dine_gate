from django.contrib import admin
from .models import Table_list, TableReservation

# Register models with custom admin classes
admin.site.register([Table_list,TableReservation])

