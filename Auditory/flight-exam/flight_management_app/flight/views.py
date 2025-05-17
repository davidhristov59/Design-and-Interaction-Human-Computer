from django.shortcuts import render, redirect, get_object_or_404
from .forms import FlightForm, ContactForm
from .models import Flight
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

# Show flights in the past

def index(request):
    flights = Flight.objects.filter(date__lte=datetime.now().date())
    # flights = Flight.objects.all()
    context = {"flight_list" : flights, # data sent to the template
               "app_name" : "flight"}

    return render(request, "index.html", context)

# Show flight details
def details(request, flight_id):

    flight = Flight.objects.filter(id = flight_id).first()
    context = {"flight_data" : flight,
               "app_name" : "flight"}

    return render(request, "details.html", context)

# Add flight
def add_flight(request):
    if request.method == "POST":
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")

    form = FlightForm()
    return render(request, "add-flight.html", {'form': form})

# Edit flight
def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    # Flight.objects.filter(pk=flight_id).exists()

    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES, instance=flight)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = FlightForm(instance=flight)
    return render(request, "edit_flight.html", context={'form': form, 'flight_id': flight_id})


# Contact form
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            # send mail, save the message etc..
        return redirect('index')

    form = ContactForm()
    return render(request, "contact.html", context={'form': form})