from django.shortcuts import render

# Create your views here.
def my_reservation(request):
    return render(request,template_name='reservations/my_reservation.html')
def manage_reservation(request):
    return render(request,template_name='reservations/manage_reservation.html')
def reserve_table(request):
    return render(request,template_name='reservations/reserve_table.html')
