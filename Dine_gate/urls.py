"""
URL configuration for Dine_gate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as a_views
from restaurant_project import views as rp_views
from reservations import views as re_views
from event_reservations import views as er_views
from restaurants import views as r_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',rp_views.home,name='home'),
    path('accounts/login/',a_views.login,name= 'login'),
    path('accounts/sign_up/',a_views.sign_up,name= 'sign_up'),
    path('accounts/profile/',a_views.profile,name= 'profile'),
    path('accounts/logout/',a_views.logout,name= 'logout'),
    path('reservations/reserve_table/',re_views.reserve_table,name= 'reserve_table'),
    path('reservations/manage_reservation/',re_views.manage_reservation,name= 'manage_reservation'),
    path('reservations/my_reservation/',re_views.my_reservation,name= 'my_reservation'),
    path('event_reservations/reserve_event/',er_views.reserve_event,name= 'reserve_event'),
    path('restaurants/add_restaurant/',r_views.add_restaurant,name='add_restaurant'),
    path('restaurants/my_restaurant/',r_views.my_restaurant,name='my_restaurant'),
    path('restaurants/restaurant_list/',r_views.restaurant_list,name='restaurant_list'),
    path('restaurants/owner_dashboard/',r_views.owner_dashboard,name='owner_dashboard'),
]
