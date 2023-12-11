# apps.py

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'

    def ready(self):
        # Importa la señal aquí para evitar el problema de AppRegistryNotReady
        from .signals import create_roles

        # Registra la señal con post_migrate
        post_migrate.connect(create_roles, sender=self)
