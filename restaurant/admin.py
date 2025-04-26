from django.contrib import admin
from .models import Restaurant, Menu, Dine_type

# Custom admin for Restaurant model
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id','restaurant_name', 'city', 'area', 'location', 'min_price', 'max_price', 'contact_no', 'email')
    search_fields = ('id','restaurant_name', 'city', 'area')
    list_filter = ('city', 'area')
    ordering = ('restaurant_name',)

# Custom admin for Menu model
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','restaurant_name', 'item_name', 'cuisine', 'price')
    search_fields = ('id','item_name', 'cuisine','restaurant_name',)
    list_filter = ('cuisine',)
    ordering = ('restaurant_name', 'item_name')

# Custom admin for Dine_type model
class DineTypeAdmin(admin.ModelAdmin):
    list_display = ('id','Restuarant_name', 'dine_type')
    search_fields = ('id','dine_type','Restuarant_name',)
    list_filter = ('dine_type',)
    ordering = ('Restuarant_name',)

# Register the models with their custom admin classes
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Dine_type, DineTypeAdmin)

