from django.contrib import admin

from CarDealership.models import Distributor, Car

# Register your models here.
class DistributorAdmin(admin.ModelAdmin):

# При креирање на нов производител, корисникот се доделува автоматски според најавениот корисник.

  def save_model(self, request, obj, form, change):
      obj.user = request.user # корисникот се доделува автоматски според најавениот корисник
      super(DistributorAdmin, self).save_model(request, obj, form, change)

class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'price', 'distributor', 'year_made', 'distance_km']


admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Car, CarAdmin)