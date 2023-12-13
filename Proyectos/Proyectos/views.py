from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Core.forms import RegistroForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido, {}'.format(user.username))

            if user.is_superuser:
                # Si es superusuario, redirige al panel de admin
                return redirect('admin:index')
            elif user.rol and user.rol.tipo_usuario == 'Padre':
                # Redirige a la URL deseada para los padres
                return redirect('vista_vinculo')
            else:
                # Redirige a la URL predeterminada para otros usuarios
                return redirect('Inicio')

        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html', {})

    return render(request, 'login.html', {})


# views.py
from Core.models import Usuario
from Core.forms import RegistroForm
from .utils import generate_unique_code
from django.shortcuts import render

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])

            # Genera un código único aleatorio y guarda el usuario
            user.codigo_unico = generate_unique_code()
            user.save()

            print(f"Formulario enviado correctamente. Código de usuario: {user.codigo_unico}")
            return render(request, 'registro_confirmado.html', {'codigo_unico': user.codigo_unico})
        else:
            print(f"Errores en el formulario: {form.errors}")
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
@login_required
def recuperarc(request):
    return render(request, 'recuperarc.html',{
    })

@login_required
def confirmarrecuperarc(request):
    
    return render(request, 'pagina_de_confirmacion.html',{
    })

def index(request):
    return render(request, 'index.html',{
    })

######################################################################################
# Actividades Disponibles
from django.shortcuts import render, redirect
from Core.models import Actividad, Inscripcion
from django.contrib.auth.decorators import login_required
@login_required
def ActividadesDisponibles(request):
    actividades_completas = Actividad.objects.all()
    return render(request, 'ActividadesDisponibles.html', {'actividades_completas': actividades_completas})

################################################################################################

@login_required
def registro_confirmado(request):
    return render(request, 'registro_confirmado.html')


@login_required
def Inicio(request):
    return render(request, 'Inicio.html')

@login_required
def ValorAdquisitivo(request):
    return render(request, 'ValorAdquisitivo.html')
@login_required
def valor_del_dinero(request):
    return render(request, 'valor_del_dinero.html')
##########################################################################################################
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(["GET", "POST"])
def actividad1(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad1')  # O la URL que desees

    return render(request, 'actividad1.html')

@login_required
@require_http_methods(["GET", "POST"])
def actividad2(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad2')  # O la URL que desees

    return render(request, 'actividad2.html')


@login_required
@require_http_methods(["GET", "POST"])
def actividad3(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad3')  # O la URL que desees

    return render(request, 'actividad3.html')


@login_required
@require_http_methods(["GET", "POST"])
def actividad4(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad4')  # O la URL que desees

    return render(request, 'actividad4.html')

@login_required
def actividad5(request):
    return render(request, 'actividad5.html')

from django.http import HttpResponseNotFound, JsonResponse
from django.http import JsonResponse

from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Core.models import Actividad

@login_required
def actividad01(request):
    # Obtener la instancia de la actividad actual
    nombre_actividad = "actividad1"  # Ajusta según el nombre de la actividad
    try:
        actividad_actual = Actividad.objects.get(nombre=nombre_actividad)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("La actividad no existe")

    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Incrementar la puntuación del usuario actual por, digamos, 5 puntos
        puntos_a_incrementar = 5
        request.user.puntuacion += puntos_a_incrementar
        request.user.save()

        # Devolver la puntuación actual en la respuesta JSON
        return JsonResponse({'puntuacion': request.user.puntuacion, 'mensaje': f'¡Has ganado {puntos_a_incrementar} puntos!'})

    # Pasar la puntuacion_maxima al contexto
    puntuacion_maxima = actividad_actual.puntuacion_maxima

    return render(request, 'actividad01.html', {'puntuacion_maxima': puntuacion_maxima, 'puntuacion_actual': request.user.puntuacion})


@login_required
@require_http_methods(["GET", "POST"])
def actividad02(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad02')  # O la URL que desees

    return render(request, 'actividad02.html')
@login_required
@require_http_methods(["GET", "POST"])
def actividad03(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad03')  # O la URL que desees

    return render(request, 'actividad03.html'
                  )
@login_required
@require_http_methods(["GET", "POST"])
def actividad04(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad04')  # O la URL que desees

    return render(request, 'actividad04.html')
@login_required
@require_http_methods(["GET", "POST"])
def actividad05(request):
    if request.method == "POST":
        # Lógica para manejar el formulario POST
        # Redirecciona a donde necesites
        return redirect('actividad05')  # O la URL que desees

    return render(request, 'actividad05.html')
##############################################################################################

######################################################################################
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from Core.models import Actividad

class ActividadDetailView(DetailView):
    model = Actividad
    context_object_name = 'actividad'
    slug_field = 'nombre_actividad'
    slug_url_kwarg = 'nombre_actividad'

    def get_template_names(self):
        # Aquí puedes personalizar la lógica para determinar el nombre de la plantilla
        # En este ejemplo, asumimos que tienes plantillas llamadas actividad1.html, actividad2.html, etc.
        nombre_actividad = self.kwargs.get('nombre_actividad')
        return [f'actividades/{nombre_actividad}.html']

    def get(self, request, *args, **kwargs):
        # Lógica específica para la solicitud GET
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Lógica para manejar el formulario POST aquí
        # ...
        # Obtener el nombre de la actividad actual
        nombre_actividad = self.kwargs.get('nombre_actividad')

        # Redirigir a la vista correspondiente
        return redirect(f'{nombre_actividad}')

    
##################################################################################################
from django.http import JsonResponse

def actualizar_puntuacion(request):
    if request.method == "POST":
        # Lógica para actualizar la puntuación del usuario
        user = request.user
        user.puntuacion += 2
        user.save()

        # Devuelve una respuesta JSON con la nueva puntuación
        return JsonResponse({'puntuacion': user.puntuacion})
    else:
        # Devuelve una respuesta JSON indicando que solo se aceptan solicitudes POST
        return JsonResponse({'mensaje': 'Se esperaba una solicitud POST'})

#################################################################################################################
 
# Familia
# Familia
from django.shortcuts import render, redirect
from Core.models import Usuario, VinculoFamiliar
from django.contrib import messages
from django.contrib.messages import get_messages

def vista_vinculo(request):
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo_unico', None)
        usuario_actual = request.user

        try:
            usuario_a_vincular = Usuario.objects.get(codigo_unico=codigo_ingresado)

            # Verificar si ya hay un vínculo entre los usuarios
            if VinculoFamiliar.objects.filter(usuario_principal=usuario_actual, usuario_vinculado=usuario_a_vincular).exists():
                messages.error(request, 'Ya tienes un vínculo con este usuario.')
                return render(request, 'error_template.html', {'error_message': 'Ya tienes un vínculo con este usuario.'})

            # Verificar si el usuario ya tiene un vínculo
            if VinculoFamiliar.objects.filter(usuario_principal=usuario_actual).exists():
                messages.error(request, 'Ya tienes un vínculo. No puedes crear más vínculos.')
                return render(request, 'error_template.html', {'error_message': 'Ya tienes un vínculo. No puedes crear más vínculos.'})

            # Pasa la información del usuario a vincular al contexto
            context = {'usuario_a_vincular': usuario_a_vincular, 'mostrar_modal': True}

            # Elimina los mensajes almacenados en la sesión
            storage = get_messages(request)
            storage.used = True

            # Renderiza la plantilla de confirmación con el contexto
            return render(request, 'confirmacion_vinculo_template.html', context)

        except Usuario.DoesNotExist:
            messages.error(request, 'Código único no válido. Verifique el código e inténtelo nuevamente.')
            return render(request, 'error_template.html', {'error_message': 'Código único no válido. Verifique el código e inténtelo nuevamente.'})

    return render(request, 'vinculo_template.html')



def confirmacion_vinculo(request):
    if request.method == 'POST':
        # Obtén el usuario actual
        usuario_actual = request.user

        # Obtén el código ingresado desde el formulario
        codigo_ingresado = request.POST.get('codigo_unico', None)

        try:
            # Intenta obtener el usuario a vincular
            usuario_a_vincular = Usuario.objects.get(codigo_unico=codigo_ingresado)

            # Crear el vínculo en VinculoFamiliar
            VinculoFamiliar.objects.create(usuario_principal=usuario_actual, usuario_vinculado=usuario_a_vincular)

            # Pasa el nombre del usuario vinculado al contexto
            context = {'nombre_usuario_vinculado': usuario_a_vincular.username}
            messages.success(request, 'Usuarios vinculados exitosamente.')

            # Renderiza la plantilla de éxito con el contexto
            return render(request, 'exito_template.html', context)

        except Usuario.DoesNotExist:
            messages.error(request, 'Código único no válido. Verifique el código e inténtelo nuevamente.')
            return render(request, 'error_template.html')

    # Si el método no es POST, simplemente renderiza la plantilla de confirmación
    return render(request, 'confirmacion_vinculo_template.html')



def exito_template(request):
    return render(request, 'exito_template.html')

def error_template(request):
    return render(request, 'error_template.html')
############################################################################################################################
# views.py
from django.shortcuts import render
from Core.models import Usuario, VinculoFamiliar

def informe_puntos(request):
    # Obtén el usuario actual (padre)
    usuario_actual = request.user

    # Busca el vínculo familiar para el usuario actual
    try:
        vinculo = VinculoFamiliar.objects.get(usuario_principal=usuario_actual)
    except VinculoFamiliar.DoesNotExist:
        # Manejar el caso en que no haya vínculo
        mensaje_retroalimentacion = "No hay vínculo familiar para el usuario actual."
        context = {'mensaje_retroalimentacion': mensaje_retroalimentacion}
        return render(request, 'informe_puntos.html', context)

    # Obtén la puntuación y el nombre de usuario del usuario vinculado (niño)
    puntuacion_usuario_vinculado = vinculo.usuario_vinculado.puntuacion
    username_usuario_vinculado = vinculo.usuario_vinculado.username

    # Lógica para determinar el mensaje de retroalimentación hacia el padre
    if puntuacion_usuario_vinculado >= 100:
        mensaje_retroalimentacion = f"¡Excelente desempeño de {username_usuario_vinculado}! Sigue así, ¡está haciendo un trabajo increíble!"
    elif puntuacion_usuario_vinculado >=40:
        mensaje_retroalimentacion = f"Buen trabajo, pero {username_usuario_vinculado} puede mejorar en algunos aspectos. ¡Anímalo a seguir esforzándose!"
    else:
        mensaje_retroalimentacion = f"{username_usuario_vinculado} necesita mejorar en varios aspectos. Considera brindarle más apoyo y motivación para que pueda progresar."

    # Pasa la puntuación, nombre de usuario y el mensaje de retroalimentación al contexto
    context = {
        'puntuacion_usuario_vinculado': puntuacion_usuario_vinculado,
        'username_usuario_vinculado': username_usuario_vinculado,
        'mensaje_retroalimentacion': mensaje_retroalimentacion
    }

    # Renderiza la plantilla con el contexto
    return render(request, 'informe_puntos.html', context)
###################################################################
from django.shortcuts import render
from django.views import View

class ConsejosView(View):
    def get(self, request):
        return render(request, 'consejos.html')


##########################################################################################

#Reporte PDF
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from Core.models import Usuario

def generar_reporte_pdf(request):
 from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from Core.models import Usuario

def generar_reporte_pdf(request):
    # Obtén los datos de los usuarios
    usuarios = Usuario.objects.all()

    # Crea un objeto BytesIO para almacenar el PDF
    buffer = BytesIO()

    # Crea el objeto PDF con ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    data = []

    # Encabezados de la tabla
    headers = ['ID', 'username', 'Nombre', 'Apellido', 'email', 'rol', 'genero', 'código_unico', 'estado']
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
            usuario.genero, # Obtén el nombre del género
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
######################################################################
# generar_informe_vinculos
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from Core.models import VinculoFamiliar

def generar_informe_vinculos(request):
    # Obtén los datos de los vínculos familiares
    vinculos = VinculoFamiliar.objects.all()

    # Crea un objeto BytesIO para almacenar el PDF
    buffer = BytesIO()

    # Crea el objeto PDF con ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    data = []

    # Encabezados de la tabla
    headers = ['ID', 'Usuario Principal', 'Rol Usuario Principal', 'Usuario Vinculado', 'Rol Usuario Vinculado']
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
##########################
#Reporte Niños 
# views.py
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from Core.models import Usuario

def generar_informe_ninos(request):
    # Obtén los datos de los usuarios con el rol de niño, ordenados por puntuación de mayor a menor
    usuarios_ninos = Usuario.objects.filter(rol__tipo_usuario='Niño').order_by('-puntuacion')

    # Crea un objeto BytesIO para almacenar el PDF
    buffer = BytesIO()

    # Crea el objeto PDF con ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    data = []

    # Encabezados de la tabla
    headers = ['ID', 'Username', 'Puntuación']
    data.append(headers)

    # Agrega los datos de los usuarios a la tabla
    for usuario in usuarios_ninos:
        data.append([
            usuario.id,
            usuario.username,
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
################################################
# En views.py
from django.shortcuts import render
from Core.models import Usuario

def ranking(request):
    # Obtener la lista de usuarios con el rol de niño, ordenada por puntuación
    ranking_usuarios = Usuario.objects.filter(rol__tipo_usuario='Niño').order_by('-puntuacion')

    # Pasar la lista a la plantilla
    return render(request, 'ranking.html', {'ranking_usuarios': ranking_usuarios})
