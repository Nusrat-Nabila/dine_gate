from django.shortcuts import render, redirect
from .forms import CustomerAdd
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def Login(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data=request.POST)
        if frm.is_valid():
            user_name = frm.cleaned_data['username']
            pass_word = frm.cleaned_data['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return redirect('Customer_home')
        return render(request,'account/Login.html', {'form': frm})
    else:
        frm = AuthenticationForm()
        return render(request,'account/Login.html', {'form': frm})

def Customer_signup(request):
    if request.method == "POST" :
     frm = CustomerAdd(request.POST)
     if frm.is_valid():
        frm.save()
        return redirect('Login')
     else:
      print(frm.errors)
    else:
       frm = CustomerAdd()
    return render(request,'account/Customer_signup.html', {'form': frm})

def Customer_profile(request):
    return render(request,template_name='account/Customer_profile.html')


