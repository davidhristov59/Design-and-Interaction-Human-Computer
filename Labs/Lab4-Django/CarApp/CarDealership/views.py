from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
    cars = Car.objects.all()

    context = {'cars_list' : cars}

    return render(request, "index.html", context)

def details(request, id):
    cars = Car.objects.filter(id = id).first()

    context = {'cars_data': cars}

    return render(request, "details.html", context)


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'addCar.html', {'form': form})
