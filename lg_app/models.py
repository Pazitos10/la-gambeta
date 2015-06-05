from django.db import models

class Complejo(models.Model):
    id = models.AutoField(primary_key=True)        
    nombre = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.IntegerField()
    email = models.EmailField()

class Cancha(models.Model):
    id = models.AutoField(primary_key=True)
    complejo = models.ForeignKey(Complejo)


class Turno(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cancha = models.ForeignKey(Cancha)

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    LOCAL = 'L'
    VISITANTE = 'V'
    CONDICION = ((LOCAL, 'Local' ), (VISITANTE, 'Visitante'))
    nombre = models.CharField(max_length=50, null=True, blank=True)
    turno = models.ForeignKey(Turno)
    condicion = models.CharField(max_length=1, choices=CONDICION, default=LOCAL)

class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    telefono = models.IntegerField()
    equipo = models.ForeignKey(Equipo)

    
