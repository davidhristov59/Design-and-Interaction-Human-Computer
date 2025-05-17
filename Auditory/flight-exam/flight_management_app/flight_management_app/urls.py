"""
URL configuration for flight_management_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from flight import views as FlightViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',FlightViews.index, name = 'index' ),
    path('details/<flight_id>', FlightViews.details, name = 'details'),
    path('add-flight/', FlightViews.add_flight, name = 'add-flight'),
    path('edit-flight/<flight_id>', FlightViews.edit_flight, name = 'edit-flight'),
    path('contact/', FlightViews.contact, name = 'contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
