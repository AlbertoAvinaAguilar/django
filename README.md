# Django!

> Descarga de docker para windows. https://docs.docker.com/desktop/windows/install/ 

Docker hub **es un repositorio público en la nube, similar a Github, para distribuir los contenidos**. Está mantenido por la propia Docker y hay multitud de imágenes, de carácter gratuito, que se pueden descargar y asi no tener que hacer el trabajo desde cero al poder aprovechar “plantillas”

En docker Hub podemos ver imagenes oficiales. Nosotros trabajaremos con debian:bullseye-slim 

El contenedor de docker emplea una iso que utiliza como base, donde configuramos un archivo de configuracion con las dependencias que ocuparemos. y el archivo yml los procesos o servicios. 

Para iniciar nuestro docker comenzamos con el comando
 > docker-compose up -d
Que instalara todas las dependencias necesarias para el funcionamiento de nuestro contenedor

> docker-compose up -d --biuld
Reconstruye toda nuestra aplicación con todas las dependencias nuevas (Cuando se agrega alguna nueva dependencia)

> docker-compose ps
Visualizamos el estado de nuestros procesos

Podemos realizar la visualización de los logs globales o de nuestro proceso en especifico
> docker-compose logs
docker-compose logs app

> docker-compose exec app bash 

Ingresamos a el origen con usuario root y la contraseña de nuestro debian, para empezar a construir nuestra aplicación

> django-admin startproject padron .

Creamos nuestro proyecto de django (solo el esqueleto o la base del proyecto)

> python3 manage.py startapp hola

Creamos la aplicación llamada hola de django

>python3 manage.py check

Verifica que las dependencias son las necesarias para el funcionamiento de la app

>python3 manage.py makemigrations
>python3 manage.py migrate

Comando para la creación de las migraciones definidas en nuestro proyecto

>python3 manage.py createsuperuser

Comando que crea el super usuario de la administración de usuarios de django
C:\Users\ITecnologia\Documents\gitlab\cursojiapaz>
>docker-compose exec app bash
root@a52af4cbd1f1:/app# exit
C:\Users\ITecnologia\Documents\gitlab\cursojiapaz>
>docker-compose down

------------------------ day 2 --------------------
pip freeze Checamos con este comando que el proyecto cuente con las dependencias necesarias para funcionar

>docker-compose up -d --build 
Reconstruye todo el proyecto completo, crea los servicios en funcion de las imagenes configuradas
-d nos permite que se ejecute en segundo plano nuestro comando

>docker-compose exec app bash 
entra al contenedor de la app

C:\Users\ITecnologia\Documents\gitlab\cursojiapaz\padron>docker-compose exec app bash
root@d6fdd62ed328:/app# pip freeze
asgiref==3.5.2
Django==4.0.6
mysqlclient==2.1.1
sqlparse==0.4.2
root@d6fdd62ed328:/app#

> python3 manage.py runserver 0:8000

El flujo para generar un nuevo modulo es
url, view funcion, regresas a tu html


> docker-compose ps 
podemos visualizar los procesos que esta utilizando nuestro contenedor
>docker-compose logs
>docker-compose logs app

>NOTAS
----------- MODELOS.PY -------------------
En los modelos para definir un campo requerido se utiliza blank ""por default van en requeridos"".
blank=True significa que para el formulario no es obligatorio ese campo
null=True indica que se pueden guardar valores nulos en la base de datos

Cuando un campo es autoincremental se designa en el modelo como AutoField al campo que vamos a aplicar.
ejemplo models.AutoField()

---------- SETTINGS.PY -------------------
Para los mensajes de los fields se modifica el lenguaje a MEXICO 
LANGUAGE_CODE = 'es-mx' 

----- USO DE MULTIPLES BASE DE DATOS ------------
1. Primero realizar la configuración de las dos bases de datos en setting.py para indicar la bd de default y la otra que vamos a usar
2. Se crea el modelo que se va implementar para la tabla de la base de datos no default
3. En views implementamos departamentos = Departamento.objects.all().using('trabajadores') donde con using indicamos que base de datos vamos a emplear
4. Imprimimos lo del queryset en html

---- USO DE INSPECTDB ------------
Obtener catalogo de otra base de datos y almacenar el id en una distinta tabla de otra base de datos
python3 manage.py inspectdb  > models_otros.py
python3 manage.py inspectdb --database="servidor41" > models_otros.py apuntando a otra base de datos
2. Se crea el modelo aunque no se corran las migraciones es para establecer la estructura de los campos que vamos a tratar 
3. en views obtenemos la informacion de la otra base de datos importando el modelo y haciendo uso de queryset
departamentos = Departamento.objects.all().using('trabajadores') Especificamos la otra base de datos que vamos a utilizar
4. en el html creamos manualmente nuestro select
5. en views seteamos el valor antes del save para almacenar el id del select manual















