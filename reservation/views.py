from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.utils import timezone
from .forms import SearchTableForm,TableAddForm
from account.models import CustomerUser
from restaurant.models import Restaurant
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponseBadRequest
from .models import Table_list, TableReservation
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages

#search table list for customer
def search_table(request, id):
    customer_id = request.session.get('user_id')

    if not customer_id:
        return redirect('login')

    try:
        customer = CustomerUser.objects.get(id=customer_id)
    except CustomerUser.DoesNotExist:
        return redirect('login')
    
    restaurant = Restaurant.objects.get(pk=id)
    tables = []  
    if request.method == 'GET':
        form = SearchTableForm(request.GET)
        if form.is_valid():
            d = form.cleaned_data['date']
            s_t = form.cleaned_data['start_time']
            e_t = form.cleaned_data['end_time']
            no_of_people = form.cleaned_data['no_of_people']

            now = timezone.now()
            today = now.date()
            current_time = now.time()

            if d > today or (d == today and s_t >= current_time):
                tables = Table_list.objects.filter(
                    restaurant=restaurant,
                    date=d,
                    start_time__lte=s_t,
                    end_time__gte=e_t,
                    no_of_people__gte=no_of_people,
                    is_available=True
                )
            # Even if no tables found, still render with empty list
            return render(request, 'reservation/table_list.html', {
                'tables': tables,
                'restaurant': restaurant,
                'form_data': form.cleaned_data
            })
    else:
        form = SearchTableForm()

    return render(request, 'reservation/search_table.html', {
        'form': form,
        'restaurant': restaurant
    })



#confirm booking for customer
def confirm_booking(request, table_no, date, start_time, end_time):
    customer_id = request.session.get('user_id')

    if not customer_id:
        return redirect('login')

    try:
        customer = CustomerUser.objects.get(id=customer_id)
    except CustomerUser.DoesNotExist:
        return redirect('login')

    # Parse date and time from strings (HHMM format for time)
    try:
        reserve_date = datetime.strptime(date, '%Y-%m-%d').date()
        start_time = datetime.strptime(start_time, '%H%M').time()
        end_time = datetime.strptime(end_time, '%H%M').time()
    except ValueError:
        return HttpResponseBadRequest("Invalid date or time format.")

    # Ensure end_time is after start_time
    if start_time >= end_time:
        return HttpResponseBadRequest("End time must be after start time.")

    try:
        table = Table_list.objects.get(
            table_no=table_no,
            date=reserve_date,
            start_time=start_time,
            end_time=end_time,
            is_available=True
        )
    except Table_list.DoesNotExist:
        return HttpResponse("Table not available", status=404)

    if request.method == 'POST':
        TableReservation.objects.create(
            user=customer,
            restaurant=table.restaurant,
            table=table,
            reserve_date=reserve_date,
            start_time=start_time,
            end_time=end_time,
            status='confirm'
        )

        table.is_available = False
        table.save()

        return redirect('Book_history') 

    return HttpResponse("Only POST requests are allowed for booking.", status=405)

#book hsitory of customer
def Book_history(request):
    customer_id = request.session.get('user_id') 

    if not customer_id:
        return redirect('login')  
    
    try:
        customer = CustomerUser.objects.get(id=customer_id)
    except CustomerUser.DoesNotExist:
        return redirect('login')
    
    now = timezone.now()
    today = now.date()
    current_time = now.time()

    bookings = TableReservation.objects.filter(user=customer).order_by('-reserve_date')

    recently_booking = []
    past = []

    for b in bookings:
        if b.reserve_date > today or (b.reserve_date == today and b.end_time >= current_time):
             if b.status=='confirm':
                recently_booking.append(b)
             else:
                past.append(b)
        else:
            past.append(b)
    print(past)
    return render(request,'reservation/Book_history.html' ,{'recently_booking': recently_booking,'past': past})

#cancel booking of customer
def cancel_book(request,reservation_id):
    customer_id = request.session.get('user_id') 

    if not customer_id:
        return redirect('login') 
    else:
     try:
        customer = CustomerUser.objects.get(id=customer_id)
     except CustomerUser.DoesNotExist:
        return redirect('login')
     
    booking = TableReservation.objects.get(pk=reservation_id, user=customer)
    if request.method == 'POST':
        booking.status = 'cancel'

        booking.table.is_available = True
        booking.table.save()
        booking.save()
  

        return redirect('Book_history')

    
    return render(request,template_name='reservation/cancel_book.html')

#booking history of restaurant owner
def previous_book_history_for_restaurant(request,id):
    restaurant = Restaurant.objects.get(pk=id)
    now = timezone.now()
    today = now.date()
    current_time = now.time()

    bookings = TableReservation.objects.filter(restaurant=restaurant).order_by('-reserve_date')

    previous = []

    for b in bookings:
        if b.reserve_date < today or (b.reserve_date == today and ((b.start_time <= current_time and (b.end_time>=current_time or b.end_time<=current_time)))):
            previous.append(b)
    return render(request,'reservation/previous_book_history_for_restaurant.html',{'previous': previous})

# recent booking history of restaurant owner
def recent_book_history_for_restaurant(request,id):
    restaurant = Restaurant.objects.get(pk=id)
    now = timezone.now()
    today = now.date()
    current_time = now.time()

    bookings = TableReservation.objects.filter(restaurant=restaurant).order_by('-reserve_date')

    upcoming = []

    for b in bookings:
        if b.reserve_date > today or (b.reserve_date == today and b.end_time >= current_time):
            if b.status=='confirm':
              upcoming.append(b)
    return render(request,'reservation/recent_book_history_for_restaurant.html',{'upcoming': upcoming})

# recent  cancel booking history of restaurant owner
def recent_cancel_booking_history_for_restaurant(request,id):
    restaurant = Restaurant.objects.get(pk=id)
    now = timezone.now()
    today = now.date()
    current_time = now.time()

    bookings = TableReservation.objects.filter(restaurant=restaurant).order_by('-reserve_date')

    recent_cancel=[]

    for b in bookings:
        if b.reserve_date > today or (b.reserve_date == today and b.end_time >= current_time):
            if b.status=='cancel':
              recent_cancel.append(b)
    return render(request,'reservation/recent_cancel_booking_history_for_restaurant.html',{'recent_cancel': recent_cancel })

#view table list for restaurant owner
def view_table_list_for_restaurant_owner(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    tables = Table_list.objects.filter(restaurant=restaurant)
    
    now = timezone.now()
    today = now.date()
    current_time = now.time()

    print(f"Today: {today}, Current Time: {current_time}")

    future_tables = []
    for t in tables:
        print(f"Checking table {t.table_no}: date={t.date}, start={t.start_time}, end={t.end_time}")
        if t.date > today:
            future_tables.append(t)
        elif t.date == today and t.end_time > current_time:
            future_tables.append(t)
    
    return render(request, 'reservation/view_table_list_for_restaurant_owner.html', {
        'table': future_tables,
        'restaurant': restaurant
    })

#table added by restaurant owner
def add_table_list_for_restaurant_owner(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    if request.method == "POST":
        form = TableAddForm(request.POST, restaurant=restaurant)
        if form.is_valid():
            table = form.save(commit=False)
            table.restaurant = restaurant
            table.save()
            messages.success(request, "Table added successfully.")
            return redirect('view_table_list_for_restaurant_owner', id=restaurant.id)
    else:
        form = TableAddForm(restaurant=restaurant)
    return render(request, 'reservation/add_table_list_for_restaurant_owner.html', {'form': form})

#menu table info update by restaurant owner
def edit_table_list_for_restaurant_owner(request,id):
    table=Table_list.objects.get(pk=id)
    form=TableAddForm(instance=table)
    if request.method == "POST":
        form=TableAddForm(request.POST,request.FILES,instance=table)
        if form.is_valid():
            form.save()
            return redirect('view_table_list_for_restaurant_owner', id=table.restaurant.id)
    return render(request, 'reservation/add_table_list_for_restaurant_owner.html', {'form': form})

def confirm_delete_table(request, id):
    table = get_object_or_404(Table_list, pk=id)
    restaurant = table.restaurant
    return render(request, 'reservation/delete_table_list_for_restaurant_owner.html', {'table': table, 'restaurant': restaurant})

#delete table info for restaurant owner /restaurant
def delete_table_list_for_restaurant_owner(request, id):
    try:
        table = get_object_or_404(Table_list,pk=id)
        restaurant_id = table.restaurant.id
        table.delete()
        messages.success(request, "Table deleted successfully.")
    except Table_list.DoesNotExist:
        messages.error(request, "Table not found or already deleted.")
        restaurant_id = request.GET.get('restaurant_id')  # fallback
    return redirect('view_table_list_for_restaurant_owner', id=restaurant_id)
