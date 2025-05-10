from django.shortcuts import render, redirect
from .forms import CustomerAdd,CustomerEditForm
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
                customer = CustomerUser.objects.get(user_name__iexact=name)
                if customer.user_password == password:
                    request.session['user_id'] = customer.id
                    return redirect('Customer_home')
                else:
                    error = "Invalid password."
            except CustomerUser.DoesNotExist:
                error = "Customer not found."

        # If the role is restaurant
        elif role == 'restaurant':
            try:
                restaurant = Restaurant.objects.get(restaurant_name__iexact=name)
                if restaurant.password == password:
                    request.session['restaurant_id'] = restaurant.id
                    return redirect('restaurant_dashboard')
                else:
                    error = "Invalid password."
            except Restaurant.DoesNotExist:
                error = "Restaurant not found."

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

def edit_customer_profile(request, user_id):
    customer = CustomerUser.objects.get(pk=user_id)

    if request.method == "POST":
        form = CustomerEditForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('Customer_profile',id=customer.id)  # Redirect to profile page
    else:
        form = CustomerEditForm(instance=customer)

    return render(request, 'account/edit_customer_profile.html', {'form': form})
        
def Home(request):
    if request.session.get('user_id'):
        return redirect('Customer_home')
    elif request.session.get('restaurant_id'):
        return redirect('restaurant_dashboard')
    
    total_restaurants = Restaurant.objects.count()
    total_users = CustomerUser.objects.count()
    return render(request, 'home.html', {'total_restaurants': total_restaurants, 'total_users': total_users})

def signup_home(request):
    return render(request, template_name='account/signup_home.html')

def about_us(request):
    return render(request, template_name='account/about_us.html')
def our_service(request):
    return render(request, template_name='account/our_service.html')
def contact_us(request):
    return render(request, template_name='account/contact_us.html')