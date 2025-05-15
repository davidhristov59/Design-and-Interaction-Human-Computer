from django.apps import AppConfig


class FlightConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flight'

    def ready(self):
        from . import signals
        # This is where you can import your signal handlers
        # to ensure they are registered when the app is ready.