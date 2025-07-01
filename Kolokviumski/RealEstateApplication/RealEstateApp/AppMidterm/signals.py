from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Property, AgentProperties

# Кога еден оглас/недвижнина ќе се означи како продадена, потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба
@receiver(post_save, sender=Property)
def check_if_sold(sender ,instance, **kwargs):

    if instance.sold is True:
        agents = AgentProperties.objects.filter(property=instance)

        for agent_prop in agents:
           agent_prop.agent.number_sold_properties += 1
           agent_prop.agent.save()