from django.urls import path
from . import views

app_name = 'calificaciones_Alejandro_Carlos_Luciana'

urlpatterns = [
    path('listar/', views.listar_calificaciones, name='listar_calificaciones'),
    path('crear/', views.crear_calificacion, name='crear_calificacion'),
    path('editar/<int:id>/', views.editar_calificacion, name='editar_calificacion'),
    path('eliminar/<int:id>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('promedio-general/', views.promedio_general, name='promedio_general'),
]
