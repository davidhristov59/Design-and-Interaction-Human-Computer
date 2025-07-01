from django.apps import AppConfig


class AppmidtermConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppMidterm'

    def ready(self):
        from . import signals