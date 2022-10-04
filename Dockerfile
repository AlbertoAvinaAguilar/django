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

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

#Debian 11
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

COPY openssl.cnf /etc/ssl/openssl.cnf

EXPOSE 80

CMD [ "apachectl", "-DFOREGROUND" ]




