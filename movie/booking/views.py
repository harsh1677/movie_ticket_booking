from django.shortcuts import render, redirect
from .models import moviebook

# Create your views here.

def index(request):
    all_bookings=moviebook.objects.all()
    return render(request, 'index.html',{'bookings':all_bookings})

def bookticket(request):
    new_booking=moviebook()
    new_booking.name=request.POST.get("name")
    new_booking.movie=request.POST.get("movie")
    new_booking.ticket=request.POST.get("ticket")
    new_booking.quantity=request.POST.get("quantity")
    new_booking.save()
    return redirect('index')
