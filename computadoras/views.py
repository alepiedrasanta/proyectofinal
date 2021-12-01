from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .forms import computadorasform
from .models import compus
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request,'computadoras/menu.html', )
@login_required   
def compus_lista(request):
    publicaciones = compus.objects.all()
    return render(request,'computadoras/compus_lista.html', {'publicaciones': publicaciones})
@login_required
def compus_detalle(request,pk):
    publicacion = get_object_or_404(compus, pk = pk)
    return render(request,'computadoras/compus_detalle.html', {'publicacion': publicacion})
@login_required
def compus_nueva(request):
    if request.method == "POST":
        formulario = computadorasform(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            messages.add_message(request, messages.SUCCESS, 'Computadora guardada')
            publicaciones = compus.objects.all()
            return render(request,'computadoras/compus_lista.html', {'publicaciones': publicaciones})
    else:
         formulario = computadorasform()
    return render(request,'computadoras/compus_nueva.html', {'formulario': formulario})
@login_required
def area_editar(request,pk):
    publicaciones = get_object_or_404(compus, pk = pk)
    if request.method =="POST":
        formulario = computadorasform(request.POST, instance=publicaciones)
        if formulario.is_valid():
            publicaciones = formulario.save(commit=False)
            publicaciones.save()
            publicaciones = compus.objects.all()
            return render(request,'computadoras/compus_lista.html', {'publicaciones': publicaciones})
    else:
        formulario = computadorasform(instance=publicaciones)
    return render(request,'computadoras/compus_editar.html', {'formulario': formulario})
