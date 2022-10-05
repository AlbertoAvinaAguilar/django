from django.shortcuts import render
from usuarios.forms import FormUsuario
from .models import Usuarios,Departamento
from django.contrib import messages

def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    
    if request.method == 'POST':
        form_usuario = FormUsuario(request.POST, prefix='usuario')
        # print(request.POST)
        
        if form_usuario.is_valid():
            usuario = form_usuario.save(commit=False) #esto no almacena aun en la bd lo almacenamos en una variable para poder atrabar antes
            # print(request.POST.get('departamento'))
            #usuario.departamento es el nombre que especificamos en nuestro modelo del campo, y el request es una forma de tomar el valor del input
            usuario.departamento = request.POST.get('departamento') #el request post obtengo el valor del elemento en html, y le seteo el valor antes a la propiedad del usuario
            usuario.save()
          
            
            # messages.success(request, f"Se asignaron los usuarios al grupo {usuario}")
        
        else:
            mensaje = 'hola'
    else:
        form_usuario = FormUsuario(request.POST, prefix='usuario')      
        # print("formulario")      
        
    
    departamentos = Departamento.objects.all().using('trabajadores')
    # print(departamentos[0].iddepartamento)      
    
    context = {
        'form': form_usuario, 
        'usuarios': usuarios,
        'departamentos': departamentos
    }

    
    return render(request,'lista_usuarios.html',context)
