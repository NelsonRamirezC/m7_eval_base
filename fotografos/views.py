from django.shortcuts import redirect, render

from .models import Fotografia, Usuario

# Create your views here.


def fotografias(request):
    contexto = {}

    contexto["fotografias"] = Fotografia.objects.all()
    return render(request, "fotografias.html", contexto)


def compartir_fotografia(request, fotografia_id):
    contexto = {}
    fotografia = Fotografia.objects.get(id=fotografia_id)
    contexto["fotografia"] = fotografia
    usuarios_compartidos = fotografia.usuarios.all()
    contexto["compartido_con"] =  usuarios_compartidos
    
    usuarios =  Usuario.objects.raw("SELECT * FROM usuarios WHERE id NOT IN (SELECT usuario_id from fotografias_usuarios fu WHERE fotografia_id = %s)", [fotografia_id])
    
    contexto["usuarios"] = usuarios
        
    if request.method == "GET":
        
        return render(request, "compartir.html", contexto)
    
    if request.method == "POST":
        
        usuario_id = request.POST.get("usuario", None)
        
        fotografia = Fotografia.objects.get(id=fotografia_id)
        usuario = Usuario.objects.get(id=usuario_id)
        
        fotografia.usuarios.add(usuario)
        
        
        return render(request, "compartir.html", contexto)
    
    
    
def deja_compartir_fotografia(request, fotografia_id, usuario_id):
    contexto={}
    
    fotografia = Fotografia.objects.get(id=fotografia_id)
    usuario = Usuario.objects.get(id=usuario_id)
    
    fotografia.usuarios.remove(usuario)

    
    return redirect("compartir_fotografia", fotografia_id)