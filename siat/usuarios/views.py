from django.shortcuts import render
from usuarios.forms import FormUsuario
from .models import Usuarios

def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request,'lista_usuarios.html',{'usuarios':usuarios})
