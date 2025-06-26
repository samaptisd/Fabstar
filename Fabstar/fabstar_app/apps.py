from django.apps import AppConfig


class FabstarAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fabstar_app"

    def ready(self):
        import fabstar_app.signals
