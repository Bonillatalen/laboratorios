# ClassroomHub — Laboratorio 06

ClassroomHub es una primera aplicación web desarrollada con Django para consultar recursos de aprendizaje. El proyecto practica la relación entre URL, vista, plantilla y respuesta HTTP mediante tres páginas navegables:

- `/`: página principal con bienvenida y temas destacados.
- `/resources/`: catálogo de recursos con estados **Disponible** y **Próximamente**.
- `/about/`: información del proyecto y tecnologías utilizadas.

En esta etapa no se implementan modelos propios, formularios, autenticación ni operaciones CRUD. La base de datos incluida por Django solo queda configurada para que el proyecto pueda iniciar sus componentes estándar; no se publica ningún archivo SQLite generado localmente.

## Requisitos

- Python 3.10 o posterior.
- `pip` y `venv`.
- Django 5.2.7, instalado desde `requirements.txt`.

## Instalación

Desde la carpeta raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecución

```bash
python manage.py check
python manage.py runserver
```

Después se puede abrir `http://127.0.0.1:8000/` en el navegador. La configuración acepta variables opcionales:

```bash
DJANGO_SECRET_KEY='una-clave-local' DJANGO_DEBUG=1 python manage.py runserver
```

## Pruebas

El proyecto contiene cinco pruebas automatizadas en `pages/tests.py`:

```bash
python manage.py test pages -v 2
```

Las pruebas comprueban las respuestas HTTP de las tres páginas, las plantillas utilizadas, los estados de disponibilidad, los enlaces de navegación mediante nombres de rutas y la respuesta 404 de una dirección inexistente.

## Arquitectura MTV

- `config/urls.py` recibe la solicitud y delega las rutas de la aplicación mediante `include("pages.urls")`.
- `pages/urls.py` asigna cada URL con `path()` a una vista nombrada.
- `pages/views.py` prepara diccionarios de contexto y usa `render()` para devolver respuestas HTML.
- `pages/templates/pages/` contiene las plantillas. `base.html` concentra la estructura compartida y las demás páginas la reutilizan con `{% extends %}`.
- `pages/tests.py` prueba el comportamiento observable mediante el cliente de pruebas de Django.

Los enlaces internos usan `{% url 'pages:nombre' %}`. Así, si cambia el patrón de una URL, no es necesario buscar y corregir enlaces escritos manualmente en todas las plantillas.

## Estado y funcionalidades pendientes

El portal está completo para el alcance del Laboratorio 06. Como continuación se podrían agregar modelos, migraciones, administración, autenticación, formularios, base de datos propia y CRUD de recursos. Esas funciones se reservan para laboratorios posteriores.
