from django.db import models
from django.contrib.auth.models import AbstractUser
from Core.choices import generos, roles, estados
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator  # Importa el validador aquí


class Genero(models.Model):
    generos = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', ' Otro'),
    ]

    tipo_genero = models.CharField(max_length=20, choices=generos, default='Otro', unique=True)

    def __str__(self):
        return self.tipo_genero



class Rol(models.Model):
    PADRE = 'Padre'
    NINO = 'Niño'

    TIPO_USUARIO_CHOICES = [
        (PADRE, 'Padre'),
        (NINO, 'Niño'),
    ]

    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default=NINO,
    )

    def get_tipo_usuario_display(self):
        return dict(self.TIPO_USUARIO_CHOICES).get(self.tipo_usuario, self.tipo_usuario)

    def __str__(self):
        return f"{self.get_tipo_usuario_display()}"

import random
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
import random
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
import random


class AbstractUserSubset(AbstractUser):
    # Define los campos necesarios
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    password = models.CharField( max_length=128,verbose_name='Contraseña',validators=[ MinLengthValidator(limit_value=8, message='La contraseña debe tener al menos 8 caracteres.'),RegexValidator(regex='^(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$',message='La contraseña debe contener al menos un número, una mayúscula y un carácter especial.'
            ),
            # Agrega otras validaciones según tus requisitos
        ]
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.',
        error_messages={'unique': 'Ya existe un usuario con ese nombre de usuario.'},
        validators=[UnicodeUsernameValidator()],
        verbose_name='Nombre de Usuario'
    )
    first_name= models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres')
    lastname = models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido')
    email = models.EmailField(default='', max_length=100, unique=True, verbose_name='Correo Electrónico')
    puntuacion = models.IntegerField(default=0, verbose_name='Puntuación')




    class Meta:
        abstract = True

class Usuario(AbstractUserSubset):
    # Añade campos específicos del modelo Usuario, si es necesario
    ESTADO_CHOICES = [
        ('Habilitado', 'Habilitado'),
        ('No Habilitado', 'No Habilitado'),
    ]

    rol = models.ForeignKey(Rol, verbose_name='Rol', on_delete=models.SET_NULL, null=True, related_name='usuarios')
    genero = models.ForeignKey(Genero, null=True, on_delete=models.SET_NULL, verbose_name='Género')
    codigo_unico = models.CharField(max_length=6, unique=True, blank=True, null=True, verbose_name='Código Único')
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, verbose_name='Estado', default='Habilitado')
 # Relación para representar a los usuarios vinculados
    familiares = models.ManyToManyField('self', through='VinculoFamiliar', symmetrical=False)
    limite_vinculos = models.IntegerField(default=1)   
    actividades_inscritas = models.ManyToManyField('Actividad', verbose_name='Actividades Inscritas', related_name='usuarios_inscritos')
 


    

    def save(self, *args, **kwargs):
        if not self.pk:
            # Genera un código único aleatorio de 5 o 6 dígitos al crear un nuevo usuario
            self.codigo_unico = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

###############################################################################################################################
from django.db import models
from django.conf import settings
from PIL import Image

class Actividad(models.Model):
    DIFICULTAD_CHOICES = [
        ('facil', 'Fácil'),
        ('intermedio', 'Intermedio'),
        ('alta', 'Alta'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')
    dificultad = models.CharField(max_length=20, choices=DIFICULTAD_CHOICES, verbose_name='Dificultad')
    imagen = models.ImageField(upload_to='actividades/', null=True, blank=True, verbose_name='Imagen')

    puntuacion_maxima = models.IntegerField(default=100, verbose_name='Puntuación Máxima')

    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f'{self.nombre} (Puntuación Máxima: {self.puntuacion_maxima})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen:
            img = Image.open(self.imagen.path)

            # Agrega aquí tu lógica personalizada de procesamiento de imágenes
            # Por ejemplo, puedes redimensionar la imagen
            max_size = (300, 300)
            img.thumbnail(max_size)
            img.save(self.imagen.path)



#################################################################################################################################
# Inscriciones
from django.db import models
from django.conf import settings
from .models import Actividad

class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} inscrito en {self.actividad.nombre}'
    

#####################################################################################################################################
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from Core.models import Actividad

class ActividadDetailView(DetailView):
    model = Actividad
    context_object_name = 'actividad'
    template_name = 'actividad1.html'
    slug_field = 'nombre_actividad'
    slug_url_kwarg = 'nombre_actividad'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Lógica para manejar el formulario POST aquí
        # ...

        return render(request, self.template_name, self.get_context_data())

####################################################################################################################
#Familia 
from django.db import models
from django.contrib.auth import get_user_model

class VinculoFamiliar(models.Model):
    usuario_principal = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='vinculos')
    usuario_vinculado = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='vinculos_vinculados')
    
    class Meta:
            verbose_name_plural = "Vinculo Familiar"
    def __str__(self):
        return f'{self.usuario_principal} - {self.usuario_vinculado}'
######################################################################################################################
from django.db import models
from django.contrib.auth import get_user_model

class PuntuacionUsuario(models.Model):
    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    puntuacion = models.IntegerField(default=0)
    fecha_ganado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Puntuación de {self.usuario.username}: {self.puntuacion} puntos'

    class Meta:
        verbose_name = 'Puntuación de Usuario'
        verbose_name_plural = 'Puntuaciones de Usuarios'


#####################################################################################################################################