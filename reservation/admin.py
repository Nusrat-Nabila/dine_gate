from django.contrib import admin
from .models import Table_list, TableReservation

# Admin for Table_list
class TableListAdmin(admin.ModelAdmin):
    list_display = ('id','restaurant_name', 'table_no', 'date', 'start_time', 'end_time')
    search_fields = ('id', 'table_no')
    list_filter = ('restaurant_name', 'date')
    ordering = ('restaurant_name', 'table_no')

# Admin for TableReservation
class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'restaurant_name', 'reserve_date', 'start_time', 'end_time', 'status')
    search_fields = ('user__username', 'id')
    list_filter = ('status', 'restaurant_name', 'reserve_date')
    ordering = ('-reserve_date',)

# Register models with custom admin classes
admin.site.register(Table_list, TableListAdmin)
admin.site.register(TableReservation, TableReservationAdmin)

