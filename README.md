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
    
Proyecto basado en el siguiente artículo, las gracias y reconocimiento a su trabajo.

https://testdriven.io/blog/django-custom-user-model/
