from django.apps import AppConfig


class CakeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Cake'

    def ready(self):
        from . import signals