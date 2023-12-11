from django.contrib import admin
from django.urls import path
from.import views
from .views import registro_confirmado
from django.conf.urls.static import static
from Core.models import Usuario
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ActividadDetailView
from .views import informe_puntos
from django.contrib.auth import views as auth_views
from .views import ConsejosView  # Ajusta el nombre de la vista según tu configuración
from .views import generar_reporte_pdf,generar_informe_vinculos,generar_informe_ninos
from .views import ranking


from .views import actividad01,actividad02,actividad03, actividad04,actividad05,actividad1,actividad2,actividad3,actividad4,actividad5
urlpatterns = [    
    path('admin/', admin.site.urls, name='admin:planetas_m'),
    path('login/', views.login_view, name='login'),
    path('Inicio/', views.Inicio, name='Inicio'),
    path('', views.index, name='index'),
    path('ActividadesDisponibles/', views.ActividadesDisponibles, name='ActividadesDisponibles'),
    path('registro/', views.registro, name='registro'),
    path('recuperarc/', views.recuperarc, name='recuperarc'),
    path('confirmarrecuperarc/', views.confirmarrecuperarc, name='confirmarrecuperarc'),
    path('registro_confirmado/', registro_confirmado, name='registro_confirmado'),
    path('ValorAdquisitivo/', views.ValorAdquisitivo, name='ValorAdquisitivo'),
    path('actividad5/', views.actividad5, name='actividad5'),
    path('valor_del_dinero/', views.valor_del_dinero, name='valor_del_dinero'),
    path('logout/', views.logout_view, name='logout'),
    path('actividad03/',actividad03, name='actividad03'),
    path('actividad05/',actividad05, name='actividad05'),
    path('actividad04/',actividad04, name='actividad04'),
    path('actividad02/',actividad02, name='actividad02'),
    path('actividad01/',actividad01, name='actividad01'),
    path('actividad1/', actividad1, name='actividad1'),
    path('actividad2/', actividad2, name='actividad2'),
    path('actividad3/', actividad3, name='actividad3'),
    path('actividad4/', actividad4, name='actividad4'),
    path('actividad/<str:nombre_actividad>/', ActividadDetailView.as_view(), name='actividad-detalle'),
    path('actividad01/actualizar_puntuacion/', views.actualizar_puntuacion, name='actualizar_puntuacion'),
    path('vinculo/', views.vista_vinculo, name='vista_vinculo'),
    path('familia/exito/', views.exito_template, name='exito_template'),
    path('familia/error/', views.error_template, name='error_template'),
    path('informe_puntos/', informe_puntos, name='informe_puntos'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('consejos/', ConsejosView.as_view(), name='consejos'),
    path('generar-reporte-pdf/', generar_reporte_pdf, name='generar_reporte_pdf'),
    path('generar_informe_vinculos/', generar_informe_vinculos, name='generar_informe_vinculos'),
    path('generar_informe_ninos/', generar_informe_ninos, name='generar_informe_ninos'),
    path('ranking/', ranking, name='ranking'),
    


    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





