import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PropertyForm
from .models import *

# Create your views here.

def index(request):
    properties = Property.objects.filter(sold=False, area__gte=100).all() # This will show only unsold properties with an area greater than 100 square meters on the homepage.

    context = {"properties":properties}

    return render(request, "index.html", context=context)


def details(request, property_id):
    property = Property.objects.get(id = property_id)

    # This code calculates the total sum of the value field from all Characteristics related to a specific property.

    characteristics = CharacteristicsProperties.objects.filter(property=property)
    price = sum([c.characteristics.value for c in characteristics])

    return render(request, "details.html", context={"property":property, "price": price})

# RABOTI i vaka bez parametarot vo datumot vo modelot
# def add_property(request):
#     if request.method == "POST":
#         form = PropertyForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             prop = form.save(commit=False)
#             prop.date_created = datetime.date.today()
#             prop.save()
#
#             # Link to agent if user is one
#             agent = Agent.objects.filter(user=request.user).first()
#             if agent:
#                 AgentProperties.objects.create(agent=agent, property=prop)
#
#             return redirect('index')
#         else:
#             print("Form errors:", form.errors)
#
#     else:
#         form = PropertyForm()
#
#     return render(request, "add-property.html", context={"form": form})

def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('index')

    form = PropertyForm()

    return render(request, "add-property.html", context={"form": form})

def edit_property(request, property_id):

    prop = get_object_or_404(Property, pk = property_id)
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance = prop)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = PropertyForm(instance=prop)

    return render(request, 'edit-property.html', context={"form":form, "prop_id" : property_id})