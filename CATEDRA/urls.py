from django.urls import path
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
    path('visita/crear', views.crear_visita, name='crear_visita'),
    path('visita/<int:pk_vendedor>+<int:pk_visita>/editar/', views.visita_edit, name='visita_edit'),
]
