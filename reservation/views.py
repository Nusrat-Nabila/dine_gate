from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.utils import timezone
from .forms import SearchTableForm
from account.models import CustomerUser
from restaurant.models import Restaurant
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponseBadRequest
from .models import Table_list, TableReservation
from datetime import datetime


def search_table(request, id):
    restaurant = Restaurant.objects.get(pk=id)
   
    if request.method == 'GET':
        form = SearchTableForm(request.GET)
        if form.is_valid():
            d = form.cleaned_data['date']
            s_t = form.cleaned_data['start_time']
            e_t = form.cleaned_data['end_time']
            no_of_people = form.cleaned_data['no_of_people']

            tables = Table_list.objects.filter(
                  restaurant=restaurant,
                  date=d,
                   start_time__lte=s_t,
                   end_time__gte=e_t,
                   no_of_people__gte=no_of_people,
                   is_available=True
                   )

            return render(request, 'reservation/table_list.html', {'tables': tables,'restaurant': restaurant,'form_data': form.cleaned_data,})
        else:
          form = SearchTableForm()

    return render(request, 'reservation/search_table.html', {'form': form,'restaurant': restaurant,})

  # adjust if your models are elsewhere

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

        return redirect('Book_history')  # or render a booking success page

    return HttpResponse("Only POST requests are allowed for booking.", status=405)


def Book_history(request):
    customer_id = request.session.get('user_id')  # custom session key

    if not customer_id:
        return redirect('login')  # Not logged in
    
    try:
        customer = CustomerUser.objects.get(id=customer_id)
    except CustomerUser.DoesNotExist:
        return redirect('login')
    
    now = timezone.now()
    today = now.date()
    current_time = now.time()

    bookings = TableReservation.objects.filter(user=customer).order_by('-reserve_date')

    upcoming = []
    past = []

    for b in bookings:
        if b.reserve_date > today or (b.reserve_date == today and b.start_time >= current_time):
            upcoming.append(b)
        else:
            past.append(b)

    return render(request,'reservation/Book_history.html' ,{'upcoming': upcoming,'past': past})

def cancel_book(request,reservation_id):
    customer_id = request.session.get('user_id')  # custom session key

    if not customer_id:
        return redirect('login')  # Not logged in
    
    try:
        customer = CustomerUser.objects.get(id=customer_id)
    except CustomerUser.DoesNotExist:
        return redirect('login')

    booking = TableReservation.objects.get(pk=reservation_id, user=customer)
    if request.method == 'POST':
        booking.status = 'cancel'
        booking.save()

        booking.table.is_available = True
        booking.table.save()
        booking.delete()

        return redirect('Book_history')
    return render(request,template_name='reservation/cancel_book.html')

def Book_history_for_restaurant(request):
    return render(request,template_name='reservation/Book_history_for_restaurant.html')

