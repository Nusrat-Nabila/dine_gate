from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request,template_name='account\Login.html')

def Customer_signup(request):
    return render(request,template_name='account\Customer_signup.html')

def Add_restaurant(request):
    return render(request,template_name='account\Add_restaurant.html')

def Restaurant_signup(request):
    return render(request,template_name='account\Restaurant_signup.html')