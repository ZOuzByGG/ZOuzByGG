# signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Rol

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    # Obtén o crea el rol 'Padre'
    padre_role, _ = Rol.objects.get_or_create(tipo_usuario=Rol.PADRE)

    # Obtén o crea el rol 'Niño'
    nino_role, _ = Rol.objects.get_or_create(tipo_usuario=Rol.NINO)
