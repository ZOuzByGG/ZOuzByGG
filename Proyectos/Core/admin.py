from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import Usuario, Genero
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Deshabilitar la edición para todos los campos excepto 'estado'
        for field_name in self.fields:
            if field_name != 'estado':
                self.fields[field_name].widget.attrs['readonly'] = True

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'get_rol_display', 'tiempo_registrado', 'get_codigo_unico_display', 'genero', 'estado')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('rol__tipo_usuario',)
    
    def get_rol_display(self, obj):
        return obj.rol.get_tipo_usuario_display() if obj.rol else '-'

    get_rol_display.short_description = 'Rol'

    def tiempo_registrado(self, obj):
        if obj.date_joined:
            tiempo_transcurrido = timezone.now() - obj.date_joined
            return f"{tiempo_transcurrido.days} días, {tiempo_transcurrido.seconds // 3600} horas"
        return '-'

    tiempo_registrado.short_description = 'Tiempo registrado'

    def get_codigo_unico_display(self, obj):
        return obj.codigo_unico if hasattr(obj, 'codigo_unico') else '-'

    get_codigo_unico_display.short_description = 'Código Único de Usuario'

    form = CustomUserChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'puntuacion')}),
        ('Rol y Género', {'fields': ('rol', 'genero')}),
        ('Código Único y Estado', {'fields': ('codigo_unico', 'estado')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'rol', 'genero', 'codigo_unico', 'estado'),
        }),
    )
    def has_add_permission(self, request):
        return False  # Deshabilita el botón de "Añadir usuario"

    def get_form(self, request, obj=None, **kwargs):
        # Si el usuario es el mismo que está editando, permitir la edición completa
        if obj is None or request.user == obj:
            kwargs['form'] = CustomUserChangeForm
        else:
            # Si es otro usuario, deshabilitar todos los campos
            class ReadOnlyUserChangeForm(CustomUserChangeForm):
                class Meta(CustomUserChangeForm.Meta):
                    model = Usuario

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    for field_name in self.fields:
                        self.fields[field_name].widget.attrs['readonly'] = True

            kwargs['form'] = ReadOnlyUserChangeForm

        return super().get_form(request, obj, **kwargs)

    def generar_reporte_pdf(modeladmin, request, queryset):
        # Obtén los datos de los usuarios seleccionados
        usuarios = queryset

        # Crea un objeto BytesIO para almacenar el PDF
        buffer = BytesIO()

        # Crea el objeto PDF con ReportLab
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        data = []

        # Encabezados de la tabla
        headers = ['ID', 'username', 'first_name', 'lastname', 'email', 'rol', 'genero', 'código_unico', 'estado']
        data.append(headers)

        # Agrega los datos de los usuarios a la tabla
        for usuario in usuarios:
            data.append([
                usuario.id,
                usuario.username,
                usuario.first_name,
                usuario.lastname,
                usuario.email,
                usuario.rol.get_tipo_usuario_display(),  # Obtén el nombre del rol
                usuario.genero,
                usuario.codigo_unico,
                usuario.estado,
            ])

        # Crea la tabla y establece el estilo
        table = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table.setStyle(style)

        # Agrega la tabla al documento
        doc.build([table])

        # Reinicia el buffer y responde con el archivo PDF
        buffer.seek(0)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=reporte_usuarios.pdf'
        response.write(buffer.read())
        buffer.close()

        return response

    generar_reporte_pdf.short_description = 'Generar informe PDF de usuarios seleccionados'


    def generar_informe_ninos(modeladmin, request, queryset):
        # Obtén los datos de los usuarios con el rol de niño, ordenados por puntuación de mayor a menor
        usuarios_ninos = Usuario.objects.filter(rol__tipo_usuario='Niño').order_by('-puntuacion')

        # Crea un objeto BytesIO para almacenar el PDF
        buffer = BytesIO()

        # Crea el objeto PDF con ReportLab
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        data = []

        # Encabezados de la tabla
        headers = ['ID Usuario', 'Usuario','Rol', 'Puntuación']
        data.append(headers)

        # Agrega los datos de los usuarios a la tabla
        for usuario in usuarios_ninos:
            data.append([
                usuario.id,
                usuario.username,
                usuario.rol.get_tipo_usuario_display() if usuario.rol else '-',
                usuario.puntuacion,
            ])

        # Crea la tabla y establece el estilo
        table = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table.setStyle(style)

        # Agrega la tabla al documento
        doc.build([table])

        # Reinicia el buffer y responde con el archivo PDF
        buffer.seek(0)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=informe_ninos.pdf'
        response.write(buffer.read())
        buffer.close()

        return response

    generar_informe_ninos.short_description = 'Generar informe PDF de niños ordenados por puntuación'

    actions = [generar_reporte_pdf, generar_informe_ninos]
# Registrar el modelo Usuario en el administrador
admin.site.register(Usuario, UsuarioAdmin)
# Registrar el modelo Genero en el administrador
admin.site.register(Genero)

###############################################################
# Actividades
# admin.py
from django.contrib import admin
from .models import Actividad, Inscripcion

class InscripcionAdmin(admin.TabularInline):
    model = Inscripcion
    extra = 0

class ActividadAdmin(admin.ModelAdmin):
    inlines = [InscripcionAdmin]

admin.site.register(Actividad, ActividadAdmin)
#####################################################################
#Familia
# admin.py
from django.contrib import admin
from .models import VinculoFamiliar

class VinculoFamiliarAdmin(admin.ModelAdmin):
    list_display = (
        'usuario_principal_username', 'usuario_principal_rol',
        'usuario_vinculado_username', 'usuario_vinculado_rol',
    )

    def usuario_principal_username(self, obj):
        return obj.usuario_principal.username

    def usuario_principal_rol(self, obj):
        return obj.usuario_principal.rol

    def usuario_vinculado_username(self, obj):
        return obj.usuario_vinculado.username

    def usuario_vinculado_rol(self, obj):
        return obj.usuario_vinculado.rol

    def generar_informe_vinculos(modeladmin, request, queryset):
        # Obtén los datos de los vínculos familiares seleccionados
        vinculos = queryset

        # Crea un objeto BytesIO para almacenar el PDF
        buffer = BytesIO()

        # Crea el objeto PDF con ReportLab
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        data = []

        # Encabezados de la tabla
        headers = ['ID Familia', 'Usuario Principal', 'Rol', 'Usuario Vinculado', 'Rol']
        data.append(headers)

        # Agrega los datos de los vínculos a la tabla
        for vinculo in vinculos:
            data.append([
                vinculo.id,
                vinculo.usuario_principal.username,
                vinculo.usuario_principal.rol.get_tipo_usuario_display() if vinculo.usuario_principal.rol else '-',
                vinculo.usuario_vinculado.username,
                vinculo.usuario_vinculado.rol.get_tipo_usuario_display() if vinculo.usuario_vinculado.rol else '-',
            ])

        # Crea la tabla y establece el estilo
        table = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table.setStyle(style)

        # Agrega la tabla al documento
        doc.build([table])

        # Reinicia el buffer y responde con el archivo PDF
        buffer.seek(0)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=informe_vinculos.pdf'
        response.write(buffer.read())
        buffer.close()

        return response

    generar_informe_vinculos.short_description = 'Generar informe PDF de vínculos familiares seleccionados'

    actions = [generar_informe_vinculos]

# Registrar el modelo VinculoFamiliar en el administrador
admin.site.register(VinculoFamiliar, VinculoFamiliarAdmin)


##############################################################################################################

