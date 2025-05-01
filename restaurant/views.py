from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import RestaurantAddForm
from account.models import CustomerUser
from .models import Restaurant
from .models import Menu
# Create your views here.

#Customer dashboard page view
def Customer_home(request):

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login') 

    try:
        customer = CustomerUser.objects.get(id=user_id)
    except CustomerUser.DoesNotExist:
        return redirect('login')  

    return render(request, 'restaurant/Customer_home.html', {'customer': customer})


# function or method for search restaurants
def search_restaurant(request):
    if request.method == "GET":
        querys= request.GET.get('query')
        if querys:
            results=Restaurant.objects.filter(restaurant_name__icontains = querys)| Restaurant.objects.filter(city__icontains = querys)|Restaurant.objects.filter(area__icontains = querys)
        else:
            results= Restaurant.objects.none()
    return render (request,'restaurant/Restaurant_list.html', {'result': results} )

# to get the list of all the restaurants available in our website

def Restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/Restaurant_list.html', {'restaurants': restaurants})


# view a restaurant details 
def View_restaurant_detail(request, id):
    try:
        restaurant = Restaurant.objects.get(pk=id)
    except Restaurant.DoesNotExist:
        return HttpResponse("Restaurant not found", status=404)
    return render(request, 'restaurant/View_restaurant_detail.html', {'restaurants': restaurant})


#signup function for restaurant owner/restaurant
def Restaurant_signup(request):
    if request.method == "POST" :
     frm = RestaurantAddForm(request.POST)
     if frm.is_valid():
        frm.save()
        return redirect('login')
     else:
      print(frm.errors)
    else:
       frm = RestaurantAddForm()
    return render(request,'restaurant/Restaurant_signup.html',{'form':frm})

# login for restaurant owner /restaurant


#menu page for customer
def view_menu(request, restaurant_name):
    restaurant = get_object_or_404(Restaurant, name=restaurant_name)
    menu_items = Menu.objects.filter(restaurant_name=restaurant)
    return render(request, 'restaurant/Menu.html', {'menu': menu_items, 'restaurant': restaurant})


#menu page for restaurant where they can see their own restaurant's menu
def Edit_menu(request):
    return render(request,template_name='restaurant/Edit_menu.html')

#restaurant profile for restaurant/restaurant owner
def Restaurant_profile(request):
    restaurant_id = request.session.get('restaurant_id')
    if not restaurant_id:
        return redirect('login') 
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request,'restaurant/Restaurant_profile.html', {'restaurant': restaurant})

#restaurant owner dashboard
def restaurant_dashboard(request):
    return render(request, 'restaurant/restaurant_dashboard.html')
