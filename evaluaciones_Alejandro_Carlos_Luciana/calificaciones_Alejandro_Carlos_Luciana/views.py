from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm

@login_required
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calificaciones_Alejandro_Carlos_Luciana:listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'crear.html', {'form': form})

@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    promedio = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio
    })

@login_required
def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('calificaciones_Alejandro_Carlos_Luciana:listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'editar.html', {'form': form})

@login_required
def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones_Alejandro_Carlos_Luciana:listar_calificaciones')
    return render(request, 'eliminar.html', {'calificacion': calificacion})

@login_required
def promedio_general(request):
    promedio = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'promedio_general.html', {'promedio_general': promedio})
