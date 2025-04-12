from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,template_name='accounts\login.html')


def profile(request):
    return render(request, template_name='accounts\profile.html')

def sign_up(request):
    return render(request, template_name='accounts\sign_up.html')

def logout(request):
    return render(request,template_name='accounts\logout.html')