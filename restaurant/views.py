from django.shortcuts import render,redirect
from .forms import RestaurantAddForm
from .models import Restaurant
# Create your views here.
def Customer_home(request):
    return render(request,template_name='restaurant/Customer_home.html')

def Restaurant_list(request):
    return render(request,template_name='restaurant/Restaurant_list.html')

def View_restaurant_detail(request):
    return render(request,template_name='restaurant/View_restaurant_detail.html')

def Restaurant_signup(request):
    if request.method == "POST" :
     frm = RestaurantAddForm(request.POST)
     if frm.is_valid():
        frm.save()
        return redirect('restaurant_login')
     else:
      print(frm.errors)
    else:
       frm = RestaurantAddForm()
    return render(request,'restaurant/Restaurant_signup.html',{'form':frm})

def restaurant_login(request):
    error = ""
    if request.method == 'POST':
        restaurant_name = request.POST.get('restaurant_name')
        password = request.POST.get('password')
        
        try:
            restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)
            if restaurant.password == password:
                request.session['restaurant_id'] = restaurant.id 
                return redirect('restaurant_dashboard') 
            else:
                error = "Invalid password."
        except Restaurant.DoesNotExist:
            error = "Restaurant not found."
    
    return render(request, 'restaurant/restaurant_login.html', {'error': error})


def Menu(request):
    return render(request,template_name='restaurant/Menu.html')

def Edit_menu(request):
    return render(request,template_name='restaurant/Edit_menu.html')

def Restaurant_profile(request):
    return render(request,template_name='restaurant/Restaurant_profile.html')

def restaurant_dashboard(request):
    return render(request,template_name='restaurant/restaurant_dashboard.html')