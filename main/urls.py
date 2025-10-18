from django.urls import path
from . import views

urlpatterns = [
    # Mapea la ruta raíz ('/') a la función 'index' en views.py
    path('', views.index, name='index'), 
]