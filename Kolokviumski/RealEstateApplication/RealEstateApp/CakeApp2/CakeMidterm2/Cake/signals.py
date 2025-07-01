import random

from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Cake, Baker

# Кога се брише пекарот, неговите торти по случаен избор се додаваат на останатите пекари.
@receiver(post_delete, sender=Baker)
def check_given(sender ,instance, **kwargs):

    cakes = Cake.objects.filter(baker=instance)
    other_bakers = Baker.objects.exclude(id = instance.id).all()

    for cake in cakes:
        new_baker = random.choice(other_bakers)
        cake.baker = new_baker
        cake.save()

