from django.shortcuts import render

# Create your views here.

def reserve_event(request):
    return render(request,template_name='event_reservations/reserve_event.html')
