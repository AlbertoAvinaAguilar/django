from django import forms
from usuarios.models import Usuarios

class FormUsuario(forms.ModelForm):          #El nombre de la clase es el nombre de nuestro formulario
    class Meta:                              #La clase Meta indica que modelo vamos a usar para crear el formulario 
        model = Usuarios
        fields = '__all__'                   #Indicamos que campos estan presentes en nuestro formulario por ejemplo podrian ser solo '('nombre','apellido_paterno')'
        exclude = ['departamento']                 #all incluye todos los campos, exclude solo no muestra los que tengamos en esa parte  
        
        widgets = {                          #Representacion de los elementos de html mediante forms con las clases de campos incorporados
            'iduser':forms.NumberInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno':forms.TextInput(attrs={'class':'form-control'}),
        }
        
#Los forms se basan en el modelo en este caso en el modelo Usuario
#Paso uno. Iniciar la importación de forms y nuestro modelo
#
        