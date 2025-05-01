from django.shortcuts import render, redirect
from .forms import CustomerAdd
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from restaurant.models import Restaurant
from .models import CustomerUser
# Create your views here.
def login(request):
    error = ""
    
    if request.method == 'POST':
        # Get values from the form
        name = request.POST.get('name')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # If the role is customer
        if role == 'customer':
            try:
                customer = CustomerUser.objects.get(user_name=name)
                if customer.user_password == password:
                    request.session['user_id'] = customer.id
                    return redirect('Customer_home')  # Redirect to customer's dashboard
                else:
                    error = "Invalid password."
            except CustomerUser.DoesNotExist:
                error = "Customer not found."
           
        
        # If the role is restaurant
        elif role == 'restaurant':
            try:
                restaurant = Restaurant.objects.get(restaurant_name=name)
                if restaurant.password == password:
                    request.session['restaurant_id'] = restaurant.id
                    return redirect('restaurant_dashboard')  # Redirect to restaurant's dashboard
                else:
                    error = "Invalid password."
            except Restaurant.DoesNotExist:
                error = "Restaurant not found."
                restaurant = Restaurant.objects.get(restaurant_name=name)
        
    return render(request, 'account/login.html', {'error': error})

def logout_view(request):
    request.session.flush()  # session clear
    return redirect('Home')

def Customer_signup(request):
    if request.method == "POST" :
     frm = CustomerAdd(request.POST)
     if frm.is_valid():
        frm.save()
        return redirect('login')
     else:
      print(frm.errors)
    else:
       frm = CustomerAdd()
    return render(request,'account/Customer_signup.html', {'form': frm})

def Customer_profile(request,id):
    customer = CustomerUser.objects.get(pk=id)
    return render(request, 'account/Customer_profile.html', {'customer': customer})



def Home(request):
    total_restaurants = Restaurant.objects.count()
    total_users = CustomerUser.objects.count()
    return render(request, 'home.html', {'total_restaurants': total_restaurants, 'total_users': total_users})

def signup_home(request):
    return render(request, template_name='account/signup_home.html')


