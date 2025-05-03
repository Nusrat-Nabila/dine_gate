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
from account import views as a_views
from restaurant import views as r_views
from reservation import views as rv_views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',a_views.Home, name='Home'),
    path('login/',a_views.login, name='login'),
    path('Customer_signup/',a_views.Customer_signup, name='Customer_signup'),
    path('Customer_profile/<str:id>/',a_views.Customer_profile, name='Customer_profile'),
    path('Edit_customer_profile/<str:id>/',a_views.Edit_customer_profile, name='Edit_customer_profile'),
    path('signup_home/',a_views.signup_home, name='signup_home'),
    path('logout/', a_views.logout_view, name='logout'),
    path('about_us/', a_views.about_us, name='about_us'),
    path('our_service/', a_views.our_service, name='our_service'),
    path('contact_us/', a_views.contact_us, name='contact_us'),


    path('Customer_home/',r_views.Customer_home,name='Customer_home'),
    path('Restaurant_list/',r_views.Restaurant_list,name='Restaurant_list'),
    path('View_restaurant_detail/<int:id>/', r_views.View_restaurant_detail, name='View_restaurant_detail'),
    path('Restaurant_signup/',r_views.Restaurant_signup,name='Restaurant_signup'),
    path('view_menu/<int:id>/',r_views.view_menu,name='view_menu'),
    path('Restaurant_profile/',r_views.Restaurant_profile,name='Restaurant_profile'),
    path('restaurant_dashboard/',r_views.restaurant_dashboard,name='restaurant_dashboard'),
    path('search_restaurant/',r_views.search_restaurant,name='search_restaurant'),
    path('add_menu_for_restaurant_owner/<str:id>/',r_views.add_menu_for_restaurant_owner,name='add_menu_for_restaurant_owner'),
    path('view_menu_for_restaurant_owner/<str:id>/',r_views.view_menu_for_restaurant_owner,name='view_menu_for_restaurant_owner'),
    path('edit_menu_for_restaurant_owner/<str:id>/',r_views.edit_menu_for_restaurant_owner,name='edit_menu_for_restaurant_owner'),
    path('delete_menu_for_restaurant_owner/<str:id>/',r_views.delete_menu_for_restaurant_owner,name='delete_menu_for_restaurant_owner'),


    path('Book_history/',rv_views.Book_history,name='Book_history'),
    path('recent_book_history_for_restaurant/<str:id>/',rv_views.recent_book_history_for_restaurant,name='recent_book_history_for_restaurant'),
    path('previous_book_history_for_restaurant/<str:id>/',rv_views.previous_book_history_for_restaurant,name='previous_book_history_for_restaurant'),
    path('search_table/<int:id>/',rv_views.search_table,name='search_table'),
    path('confirm_booking/<str:table_no>/<str:date>/<str:start_time>/<str:end_time>/', rv_views.confirm_booking, name='confirm_booking'),
    path('cancel_book/<str:reservation_id>/',rv_views.cancel_book,name='cancel_book'),
    path('add_table_list_for_restaurant_owner/<str:id>/',rv_views.add_table_list_for_restaurant_owner,name='add_table_list_for_restaurant_owner'),
    path('view_table_list_for_restaurant_owner/<str:id>/',rv_views.view_table_list_for_restaurant_owner,name='view_table_list_for_restaurant_owner'),
    path('edit_table_list_for_restaurant_owner/<str:id>/',rv_views.edit_table_list_for_restaurant_owner,name='edit_table_list_for_restaurant_owner'),
    path('delete_table_list_for_restaurant_owner/<str:id>/',rv_views.delete_table_list_for_restaurant_owner,name='delete_table_list_for_restaurant_owner'),
    
  

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
