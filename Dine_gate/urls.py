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
from account import views as a_views
from restaurant import views as r_views
from reservation import views as rv_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',a_views.Login, name='Login'),
    path('Customer_signup/',a_views.Customer_signup, name='Customer_signup'),
    path('Add_restaurant/',a_views.Add_restaurant, name='Add_restaurant'),
    path('Restaurant_signup/',a_views.Restaurant_signup, name='Restaurant_signup'),

    path('Customer_home/',r_views.Customer_home,name='Customer_home'),
    path('Restaurant_list/',r_views.Restaurant_list,name='Restaurant_list'),
    path('View_restaurant_detail/',r_views.View_restaurant_detail,name='View_restaurant_detail'),

    path('Table_book/',rv_views.Table_book,name='Table_book'),
    path('Confo_table_book/',rv_views.Confo_table_book,name='Confo_table_book'),
    path('Book_history/',rv_views.Book_history,name='Book_history'),


]
