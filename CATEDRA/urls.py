from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('escuela', views.lista_escuelas, name='lista_escuelas'),
    path('escuela/<int:codigo>/', views.perfil_escuela, name='perfil_escuela'),
    path('escuela/crear', views.crear_escuela, name='crear_escuela'),
    path('escuela/<int:codigo>/editar/', views.escuela_edit, name='escuela_edit'),
    path('escuela/<int:codigo>/personal/crear/', views.crear_personal, name='crear_personal'),
    path('escuela/<int:codigo>/personal/editar/', views.personal_edit, name='personal_edit'),
    path('escuela/<int:codigo>/matricula/crear/', views.crear_matricula, name='crear_matricula'),
    path('escuela/<int:codigo>/matricula/editar/', views.matricula_edit, name='matricula_edit'),
    path('escuela/<int:codigo>/destrezas/crear/', views.crear_destrezas, name='crear_destrezas'),
    path('escuela/<int:codigo>/destrezas/editar/', views.destrezas_edit, name='destrezas_edit'),
    path('escuela/<int:codigo>/actividad/crear/', views.crear_actividad, name='crear_actividad'),
    path('escuela/<int:codigo>/actividad/<int:pk>/editar/', views.actividad_edit, name='actividad_edit'),
    path('cargar_escuelas/', views.cargar_escuelas, name='cargar_escuelas'),
    path('vendedores', views.lista_vendedores, name='lista_vendedores'),
    path('vendedor/<int:pk>/', views.perfil_vendedor, name='perfil_vendedor'),
    path('vendedor/<int:pk_vendedor>/visita/crear', views.crear_visita, name='crear_visita'),
    path('visita/<int:pk_vendedor>+<int:pk_visita>/editar/', views.visita_edit, name='visita_edit'),
    path('historial_visitas', views.historial_visitas, name='historial_visitas'),
    path('vendedor/<int:pk>/historial_propuestas', views.historial_propuestas, name='historial_propuestas'),
    path('vendedor/<int:pk_vendedor>/propuesta/crear', views.crear_propuesta, name='crear_propuesta'),
    path('vendedor/<int:pk_vendedor>/propuesta/<int:pk_propuesta>/editar', views.propuesta_edit, name='propuesta_edit'),
    path('propuesta/<int:pk_propuesta>/', views.propuesta_detalle, name='propuesta_detalle'),
    path('propuesta/<int:pk_propuesta>/ofrecimiento/<int:pk_ofrecimiento>/borrar', views.borrar_ofrecimiento, name='borrar_ofrecimiento'),
    path('propuesta/<int:pk_propuesta>/ofrecimiento/crear/', views.crear_ofrecimiento, name='crear_ofrecimiento'),
    path('propuesta/<int:pk_propuesta>/ofrecimiento/<int:pk_ofrecimiento>/edit', views.ofrecimiento_edit, name='ofrecimiento_edit'),
    path('propuesta/<int:pk_propuesta>/pdf/', views.propuesta_pdf, name='propuesta_pdf'),
    path('ofrecimientos', views.lista_ofrecimientos, name='lista_ofrecimientos'),
    path('propuesta/<int:pk_propuesta>/po/crear/', views.crear_po, name='crear_po'),
    path('propuesta/<int:pk_propuesta>/po/<int:pk_po>/borrar', views.borrar_po, name='borrar_po'),
    path('propuesta/<int:pk_propuesta>/po/<int:pk_po>/edit', views.po_edit, name='po_edit'),
    path('lista_po', views.lista_po, name='lista_po'),
]
