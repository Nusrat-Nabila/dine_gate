from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import RestaurantAddForm,MenuAddForm,RestaurantEditForm
from account.models import CustomerUser
from .models import Restaurant
from .models import Menu
from django.db.models import Q
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
        querys= request.GET.get('query','')
        if querys:
            restaurants=Restaurant.objects.filter(restaurant_name__icontains = querys)| Restaurant.objects.filter(city__icontains = querys)|Restaurant.objects.filter(area__icontains = querys)
        else:
            restaurants= Restaurant.objects.none()
    return render (request,'restaurant/Restaurant_list.html', {'restaurants': restaurants} )

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

#menu page for customer
def view_menu(request,id):
    restaurant = Restaurant.objects.get(pk=id)
    menu_items = Menu.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant/Menu.html', {'menu': menu_items, 'restaurants': restaurant})

#menu page for restaurant owner/restaurant
def view_menu_for_restaurant_owner(request,id):
    restaurant = Restaurant.objects.get(pk=id)
    menu_items = Menu.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant/view_menu_for_restaurant_owner.html', {'menu': menu_items, 'restaurant': restaurant})

#menu addded by restaurant owner
def add_menu_for_restaurant_owner(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    if request.method == "POST":
        form = MenuAddForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant = restaurant  
            menu_item.save()
            return redirect('view_menu_for_restaurant_owner', id=restaurant.id)
    else:
        form = MenuAddForm()
    return render(request, 'restaurant/add_menu_for_restaurant_owner.html', {'form': form})


#menu item update by restaurant owner
def edit_menu_for_restaurant_owner(request, id):
    menu_item = Menu.objects.get(pk=id)
    form = MenuAddForm(instance=menu_item)

    if request.method == "POST":
        form = MenuAddForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('view_menu_for_restaurant_owner', id=menu_item.restaurant.id)

    return render(request, 'restaurant/add_menu_for_restaurant_owner.html', {'form': form})
#delete menu item for restaurant owner /restaurant

def delete_menu_for_restaurant_owner(request, id):
    item = get_object_or_404(Menu, pk=id)  # safer lookup
    restaurant = item.restaurant

    if request.method == "POST":
        item.delete()
        return redirect('view_menu_for_restaurant_owner', id=restaurant.id)

    return render(request, 'restaurant/delete_menu_for_restaurant_owner.html', {
        'item': item,
        'restaurant': restaurant
    })


#restaurant profile for restaurant/restaurant owner
def Restaurant_profile(request):
    restaurant_id = request.session.get('restaurant_id')
    if not restaurant_id:
        return redirect('login') 
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request,'restaurant/Restaurant_profile.html', {'restaurant': restaurant})

#restaurant owner dashboard
def restaurant_dashboard(request):
    restaurant_id = request.session.get('restaurant_id')
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurant/restaurant_dashboard.html',{'restaurant': restaurant})

def edit_restaurant_profile(request,id):
    restaurant = Restaurant.objects.get(pk=id)

    if request.method == "POST":
        form = RestaurantEditForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('Customer_profile',id=restaurant.id)  # Redirect to profile page
    else:
        form = RestaurantEditForm(instance=restaurant)

    return render(request, 'restaurant/edit_restaurant_profile.html', {'form': form})