Ejemplo dedicado a los amigos de NGN
====================================


Descripción:
------------

Lista de Casas.


Requerimientos:
---------------
- Python 2.7
- Django 1.8.4

Instalación:
------------
Para este ejemplo utilizaremos virtualenv.

__Paso 1. Instalamos virtualenv.__

    $ sudo pip install virtualenv

__Paso 2. Creamos nuestro entorno virtual y lo activamos.__

    $ virtualenv test
    $ source test/bin/activate


__Paso 3. Instalamos los requerimientos del archivo requirements.txt__

    $ pip install -r requirements.txt

__Paso 4. Creamos la base de datos y al superusuario.__

    $ python manage.py migrate
    $ python manage.py createsuperuser
   

License.
========

    The MIT License (MIT)
    
    Copyright (c) 2015 Alex Dzul
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
