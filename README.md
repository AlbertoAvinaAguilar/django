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

Comando para la creación de las migraciones definidas en nuestro proyecto

>python3 manage.py createsuperuser

Comando que crea el super usuario de la administración de usuarios de django
C:\Users\ITecnologia\Documents\gitlab\cursojiapaz>docker-compose exec app bash
root@a52af4cbd1f1:/app# exit
C:\Users\ITecnologia\Documents\gitlab\cursojiapaz>docker-compose down

------------------------ day 2 --------------------
pip freeze Checamos con este comando que el proyecto cuente con las dependencias necesarias para funcionar

docker-compose up -d --build Reconstruye todo el proyecto completo, crea los servicios en funcion de las imagenes configuradas
-d nos permite que se ejecute en segundo plano nuestro comando

docker-compose exec app bash entra al contenedor de la app

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











