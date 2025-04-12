from django.shortcuts import render

# Create your views here.
def add_restaurant(request):
    return render(request,template_name='restaurants\Add_restaurant.html')
def my_restaurant(request):
    return render(request,template_name='restaurants\my_restaurant.html')
def restaurant_list(request):
    return render(request,template_name='restaurants\Restaurant_list.html')

def owner_dashboard(request):
    return render(request,template_name='restaurants\owner_dashboard.html')