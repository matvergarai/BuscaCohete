from django.db import models

class Supervisor(models.Model):
    idSupervisor = models.IntegerField(primary_key=True)
    nombreSupervisor = models.CharField(max_length=45, null=True)
    correo = models.CharField(max_length=200, unique=True)
    clave = models.CharField(max_length=50)
    controlParentalActivado = models.BooleanField()
    gradoBloqueoImagen = models.IntegerField(null=True)

class NivelEducacional(models.Model):
    idNivelEducacional = models.IntegerField(primary_key=True)
    nombreNivelEducacional = models.CharField(max_length=45)
    promptConfigAsistente = models.CharField(max_length=4000)

class Supervisado(models.Model):
    idSupervisado = models.IntegerField(primary_key=True)
    nombreSupervisado = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)
    idSupervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    colorAvatar = models.CharField(max_length=7, null=True)
    imgTopAvatar = models.CharField(max_length=255, null=True)
    colorBottomAvatar = models.CharField(max_length=7, null=True)
    imgCaraAvatar = models.CharField(max_length=255, null=True)
    tipoPeloAvatar = models.IntegerField(null=True)
    colorPeloAvatar = models.CharField(max_length=7, null=True)
    idNivelEducacional = models.ForeignKey(NivelEducacional, on_delete=models.SET_NULL, null=True)
    promptConfigAsistente = models.CharField(max_length=4000, null=True)

class Dispositivo(models.Model):
    idDispositivo = models.IntegerField(primary_key=True)
    nombreDispositivo = models.CharField(max_length=100)
    idSupervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

class Sesion(models.Model):
    idSesion = models.IntegerField(primary_key=True)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    idSupervisado = models.ForeignKey(Supervisado, on_delete=models.CASCADE)
    idDispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

class Visita(models.Model):
    idVisita = models.IntegerField(primary_key=True)
    tituloPagina = models.CharField(max_length=500, null=True)
    url = models.CharField(max_length=4000)
    idSesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    fechaVisita = models.DateTimeField()
    bloqueado = models.BooleanField()
    enlacesBloqueados = models.IntegerField()
    imagenesBloqueadas = models.IntegerField()
    anunciosBloqueados = models.IntegerField()
    palabrasBloqueadas = models.IntegerField()

class PalabrasBloqueadas(models.Model):
    idPalabrasBloqueadas = models.IntegerField(primary_key=True)
    palabra = models.CharField(max_length=255)
    bloqueoInteligente = models.BooleanField(null=True)
    idSupervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

class SitiosBloqueados(models.Model):
    idSitiosBloqueados = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=4000)
    bloqueoInteligente = models.BooleanField(null=True)
    idSupervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
