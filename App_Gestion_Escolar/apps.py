from django.apps import AppConfig

class AppGestionEscolarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_Gestion_Escolar'

    def ready(self):
        # Al importar el módulo signals, los decoradores @receiver
        # quedan registrados automáticamente en el sistema de señales de Django.
        # Es como enchufar el cable al tomacorriente: hasta que no importas,
        # las señales existen pero nadie las escucha.
        import App_Gestion_Escolar.signals  # noqa: F401