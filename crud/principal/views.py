# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import Alumno
from principal.forms import AlumnoForm

def index(request):
        alumnos = Alumno.objects.all().order_by('-id')
        return render_to_response("index.html", {"alumnos":alumnos}, context_instance=RequestContext(request))

def agregar_alumno(request):
        if request.method == "POST":
                formulario = AlumnoForm(request.POST)
                if formulario.is_valid():
                        formulario.save()
                        return HttpResponseRedirect("/")
        else:
                formulario = AlumnoForm()

        return render_to_response("agregar_alumnos.html", {"formulario":formulario}, context_instance=RequestContext(request))

def borrar_alumno(request, id_alumno):
        alumno = Alumno.objects.get(pk=id_alumno)
        alumno.delete()
        return HttpResponseRedirect("/")

def editar_alumno(request, id_alumno):
        alumno = Alumno.objects.get(pk=id_alumno)
        if request.method == "POST":
                formulario = AlumnoForm(request.POST, instance=alumno)
                if formulario.is_valid():
                        formulario.save()
                        return HttpResponseRedirect("/")
        else:
                formulario = AlumnoForm(instance=alumno)

        return render_to_response("editar_alumnos.html", {"formulario":formulario}, context_instance=RequestContext(request))
