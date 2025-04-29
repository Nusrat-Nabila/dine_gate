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


from . import settings
from django.conf.urls.static import static
from django.urls import path
from django.shortcuts import render
from account import views as a_views
from restaurant import views as r_views
from reservation import views as rv_views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',a_views.Home, name='Home'),
    path('Login/',a_views.Login, name='Login'),
    path('Customer_signup/',a_views.Customer_signup, name='Customer_signup'),
    path('Customer_profile/',a_views.Customer_profile, name='Customer_profile'),
    path('login_home/',a_views.login_home, name='login_home'),


    path('Customer_home/',r_views.Customer_home,name='Customer_home'),
    path('Restaurant_list/',r_views.Restaurant_list,name='Restaurant_list'),
    path('View_restaurant_detail/<int:id>/',r_views.View_restaurant_detail,name='View_restaurant_detail'),
    path('Restaurant_signup/',r_views.Restaurant_signup,name='Restaurant_signup'),
    path('view_menu/<str:restaurant_name>/',r_views.view_menu,name='view_menu'),
    path('Edit_menu/',r_views.Edit_menu,name='Edit_menu'),
    path('Restaurant_profile/',r_views.Restaurant_profile,name='Restaurant_profile'),
    path('restaurant_login/',r_views.restaurant_login,name='restaurant_login'),
    path('restaurant_dashboard/',r_views.restaurant_dashboard,name='restaurant_dashboard'),
    path('search_restaurant/',r_views.search_restaurant,name='search_restaurant'),

    path('Table_book/',rv_views.Table_book,name='Table_book'),
    path('Confo_table_book/',rv_views.Confo_table_book,name='Confo_table_book'),
    path('Book_history/',rv_views.Book_history,name='Book_history'),
    path('Book_history_for_restaurant/',rv_views.Book_history_for_restaurant,name='Book_history_for_restaurant'),
    path('Restaurant_recent_book/',rv_views.Restaurant_recent_book,name='Restaurant_recent_book'),


]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
