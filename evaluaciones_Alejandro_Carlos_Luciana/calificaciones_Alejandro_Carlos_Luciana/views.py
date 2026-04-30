from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm, RegistroUsuarioForm


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente. Ya puedes iniciar sesion.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register.html', {'form': form})


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
    return render(request, 'calificaciones/crear.html', {'form': form})


@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    promedio = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/listar.html', {
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
    return render(request, 'calificaciones/editar.html', {'form': form})


@login_required
def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones_Alejandro_Carlos_Luciana:listar_calificaciones')
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})


@login_required
def promedio_general(request):
    promedio = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/promedio_general.html', {'promedio_general': promedio})
