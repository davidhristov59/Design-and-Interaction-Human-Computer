from django.contrib import admin
from .models import Market, ProductInMarket, Employee, Product, ContactInfo

# Register your models here.

class MarketProductInline(admin.TabularInline):
    model = ProductInMarket
    extra = 0


class MarketAdmin(admin.ModelAdmin):

    list_display = ("name", )
    inlines = [MarketProductInline]
    exclude = ("user",)

    def save_model(self, request, obj, form, change):

        obj.user = request.user

        return super(MarketAdmin ,self).save_model(request, obj, form, change)


    def has_add_permission(self, request):

        if request.user.issuperuser:
            return True

        return False

    def has_delete_permission(self, request, obj=None):

        if obj and obj.user == request.user:
            if request.user.is_superuser:
                return True

        return False

    def has_change_permission(self, request, obj=None):

        if obj and obj.user == request.user:
            if request.user.is_superuser:
                return True

        return False


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ("name", "surname" )
    exclude = ("user", )

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):

        if obj and obj.user == request.user:
            return True

        return False

    def has_delete_permission(self, request, obj=None):

        if obj and obj.user == request.user:
            return True

        return False


class ProductAdmin(admin.ModelAdmin):

    list_display = ("name", "type_product", "product_home_country", "code")
    list_filter = ("type_product", "product_home_country")


admin.site.register(Market, MarketAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ContactInfo)
admin.site.register(MarketProductInline)
