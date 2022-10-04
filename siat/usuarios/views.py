from django.shortcuts import render
from usuarios.forms import FormUsuario
from .models import Usuarios,Departamento

def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    
    departamentos = Departamento.objects.all().using('trabajadores')
    
    
    context = {
        'usuarios': usuarios,
        'departamentos': departamentos
    }

    
    return render(request,'lista_usuarios.html',context)
