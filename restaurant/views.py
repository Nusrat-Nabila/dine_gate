from django.shortcuts import render

# Create your views here.
def Customer_home(request):
    return render(request,template_name='restaurant\Customer_home.html')

def Restaurant_list(request):
    return render(request,template_name='restaurant\Restaurant_list.html')

def View_restaurant_detail(request):
    return render(request,template_name='restaurant\View_restaurant_detail.html')