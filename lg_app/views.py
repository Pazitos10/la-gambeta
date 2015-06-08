from django.shortcuts import render, render_to_response
from django.template import RequestContext
from lg_app.forms import *

def home(request):
    return render_to_response("index.html", context_instance=RequestContext(request))

#ABM Complejo
def alta_complejo(request, template_name='alta_complejo.html'):
    form_alta_complejo = ComplejoAltaForm(request.POST or None)
    if form_alta_complejo.is_valid():
        complejo = form_alta_complejo.save(commit=True)
        complejo.save()
    return render_to_response(template_name, 
        {'form_alta_complejo': form_alta_complejo }, 
        context_instance=RequestContext(request))


def modificar_complejo(request):
    pass

def baja_complejo(request):
    pass

#ABM Cancha
def alta_cancha(request):
    pass

def modificar_cancha(request):
    pass

def baja_cancha(request):
    pass

#ABM Turno
def alta_turno(request):
    pass

def modificar_turno(request):
    pass

def baja_turno(request):
    pass

#ABM Jugador
def alta_jugador(request):
    pass

def modificar_jugador(request):
    pass

def baja_jugador(request):
    pass

#ABM Equipo
def alta_equipo(request):
    pass

def modificar_equipo(request):
    pass

def baja_equipo(request):
    pass

# Listados
def listado_complejos(request):
    pass

def listado_equipos(request):
    pass

def listado_jugadores(request):
    pass

def listado_canchas(request):
    pass

def listado_turnos(request):
    pass