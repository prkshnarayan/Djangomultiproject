from django.apps import AppConfig


class SalesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'salesapp'

    def ready(self):
        # Import signals
        import salesapp.signals
