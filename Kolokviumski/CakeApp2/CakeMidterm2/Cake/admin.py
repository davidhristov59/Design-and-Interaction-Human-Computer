from django.contrib import admin
from .models import Cake, Baker

# Register your models here.
class CakeAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        baker = Baker.objects.filter(user=request.user).first() #1 pekar
        baker_cakes = Cake.objects.filter(baker=baker).all()

        if not change and baker_cakes.count() == 10:
            return

        sum = 0

        for cake in baker_cakes:
            sum += cake.price

        old_cake_obj = baker_cakes.filter(id = obj.id).first()

        



class BakerAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser


admin.site.register(Cake, CakeAdmin)
admin.site.register(Baker, BakerAdmin)