from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request,template_name='account/Login.html')

def Customer_signup(request):
    return render(request,template_name='account/Customer_signup.html')
def Customer_profile(request):
    return render(request,template_name='account/Customer_profile.html')

