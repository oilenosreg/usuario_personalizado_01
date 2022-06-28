# Creación de usuarios personalizado

1. Se usa el número de DNI (Documento Nacional de Identidad Peruano) como nombre de usuario.
2. Se han agregado los nombres y apellidos como campos del modelo personalizado.

### Instrucciones para la ejecución del proyecto
1. Clone el proyecto usando:
    ```
    git remote add origin https://github.com/oilenosreg/usuario_personalizado_01.git
    ```
    también puede descargar el proyecto como archivo zip.
    
2. Ejecute:
    ``` 
    python manage.py makemigrations 
    ```
    ``` 
    python manage.py migrate 
    ```
    ``` 
    python manage.py createsuperuser 
    ```    
    ``` 
    python manage.py runserver 
    ```
3. Acceda al proyecto en ejecución ingresando a la página:
    ``` 
    http://localhost:8000
    ```
    
Proyecto basado en el siguiente artículo.

https://testdriven.io/blog/django-custom-user-model/

### Algunas capturas de pantalla

<a href="https://imgbb.com/"><img src="https://i.ibb.co/RCSz46v/01.png" alt="01" border="0" /></a>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/zSWYKMr/02.png" alt="02" border="0" /></a>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/314979D/03.png" alt="03" border="0" /></a>
