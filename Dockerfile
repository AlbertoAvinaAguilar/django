#indicamos la distribucion con la que vamos a trabajar
FROM debian:bullseye-slim  

#indicamos las dependencias que usa nuestro proyecto de base
RUN apt-get update
RUN apt-get install apache2 python3 python3-pip libmariadb-dev \
    libapache2-mod-wsgi-py3 python-dev openssh-client curl nano -y

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

WORKDIR /app

COPY ./siat/requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

EXPOSE 80

CMD [ "apachectl", "-DFOREGROUND" ]




