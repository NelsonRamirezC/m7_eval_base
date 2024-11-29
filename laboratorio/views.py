from django.shortcuts import render

from .models import Laboratorio

# Create your views here.

def laboratorios(request):
    contexto = {}
    
    contexto["laboratorios"] = Laboratorio.objects.all()
    return render(request, "laboratorios.html", contexto)