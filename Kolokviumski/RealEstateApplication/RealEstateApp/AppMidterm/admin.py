import datetime

from django.contrib import admin
from .models import *

# Register your models here.

# M-N relation
class AgentInline(admin.TabularInline):
    model = AgentProperties
    extra = 0

# M-N relation
class CharacteristicInline(admin.TabularInline):
    model = CharacteristicsProperties
    extra = 0


class PropertyAdmin(admin.ModelAdmin):

    inlines = [AgentInline, CharacteristicInline] #bidejki ima vrska i so Characteristic i so Agent (2 relacii ima)
    list_display = ['name', 'description', 'area']

    # (Огласи за продажба може да бидат додадени само од агенти) и по автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност
    def has_add_permission(self, request):
        if not Agent.objects.all().exists(): # If there are no agents in the database, anyone can add a property.
            return True
        return Agent.objects.filter(user=request.user).exists() # If there are agents, only users who are agents themselves can add a property.

    # Огласи за продажба може да бидат додадени само од агенти и по (автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност)
    def save_model(self, request, obj, form, change):
        agent = Agent.objects.get(user=request.user) # gets the Agent object from the currently logged-in user

        super(PropertyAdmin,self).save_model(request, obj, form, change) #actually saves the property

        if change is None:
            # If this is a new property (not an edit), it creates a new AgentProperties record, linking the agent (the user) to the property,
            # making them responsible for its sale.
            AgentProperties.objects.create(agent = agent, property=obj) # sam si se dodava za prodazba (po avtomatizam)


    # Еден оглас може да биде избришан само ако нема додадено ниту една карактеристика која го опишува
    def has_delete_permission(self, request, obj = None):
        return not CharacteristicsProperties.objects.filter(property=obj)
                # It returns True (allow delete) only if there are no CharacteristicsProperties records linked to the property (i.e., the property has no characteristics assigned).
                #If any characteristic is linked, deletion is not allowed. This enforces the rule that a listing can only be deleted if it has no characteristics describing it.


    # Огласите можат да бидат менувани само од агенти кои се задолжени за продажба на тој оглас, а останатите агенги може само да ги гледаат тие огласи
    def has_change_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        if obj is None:
            return True

        agent = Agent.objects.filter(user = request.user).first()

        return AgentProperties.objects.filter(agent = agent, property=obj).exists()

    # На супер-корисниците во Админ панелот им се прикажуваат само огласите кои се објавени на денешен датум
    def get_queryset(self, request):

        if request.user.is_superuser:
            # If the logged-in user is a superuser, it returns only the properties created today (date_created equals today's date).
            return Property.objects.filter(date_created=datetime.date.today())

        return Property.objects.all() # For all other users, it returns all properties.


class AgentAdmin(admin.ModelAdmin):

    list_display = ['name', 'surname']

    def has_add_permission(self, request): # Агенти и Карактеристики може да бидат додадени само од супер-корисници
        return request.user.is_superuser


class CharacteristicAdmin(admin.ModelAdmin):

    list_display = ['name', 'value']

    def has_add_permission(self, request):  # Агенти и Карактеристики може да бидат додадени само од супер-корисници
        return request.user.is_superuser


admin.site.register(Agent, AgentAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Characteristics, CharacteristicAdmin)

