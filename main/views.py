from django.shortcuts import render

def index(request):
    """Renderiza la pantalla principal del actor de negocio."""
    return render(request, 'index.html')