from django.db import models
from django.contrib.auth.models import User # Para el user_id de Cliente

# ----------------------------------------------------
# MODELOS PLACEHOLDER (Para Foreign Keys que faltan)
# ----------------------------------------------------
# Crearemos modelos sencillos para Comuna y Región para satisfacer las FK.
class Region(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


# ----------------------------------------------------
# TABLA PRINCIPAL: CLIENTE (Mantenedor 1)
# ----------------------------------------------------
class Cliente(models.Model):
    # ATRIBUTOS OBLIGATORIOS (según Diccionario Datos)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)

    # ATRIBUTOS OPCIONALES
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)

    # FOREIGN KEYS (FK)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user_id
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True) # comuna_id
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True) # region_id

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} ({self.rut})"


# ----------------------------------------------------
# TABLA PRINCIPAL: VEHICULO (Mantenedor 2)
# ----------------------------------------------------
class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True) # único y obligatorio
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    engine_number = models.CharField(max_length=50, null=True, blank=True)
    vin = models.CharField(max_length=50, null=True, blank=True)
    kilometraje = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relación al dueño (Cliente)
    owner = models.ForeignKey(Cliente, on_delete=models.CASCADE) # owner_id

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"