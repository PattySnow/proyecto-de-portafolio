from django.contrib import admin
from .models import Cliente, Vehiculo, Region, Comuna

# ======================================================
# 1. CLASE MODELADMIN para ordenar el formulario Cliente
# ======================================================

class ClienteAdmin(admin.ModelAdmin):
    # Definimos el ORDEN de los campos en el formulario "Añadir cliente"
    fieldsets = (
        (None, {
            'fields': (
                # Campos de Usuario y Relación
                'user', 'rut',
                # Campos de Nombre (¡El orden deseado!)
                'nombre', 'apellido_paterno', 'apellido_materno',
                # Campos de Contacto y Datos Personales
                'telefono', 'fecha_nacimiento', 'genero',
                # Campos de Dirección
                'direccion', 'region', 'comuna',
            ),
        }),
    )

    # El list_display ayuda a la lista de clientes en el admin
    list_display = ('rut', 'nombre', 'apellido_paterno', 'telefono', 'region')
    search_fields = ('rut', 'nombre', 'apellido_paterno')
    list_filter = ('genero', 'region')


# ======================================================
# 2. Registrar modelos con la configuración personalizada
# ======================================================
admin.site.register(Region)
admin.site.register(Comuna)

# ESTA LÍNEA DEBE USAR LA CLASE ClienteAdmin:
admin.site.register(Cliente, ClienteAdmin) 

# La línea anterior que tenías: admin.site.register(Cliente) NO ordena los campos.

admin.site.register(Vehiculo)











