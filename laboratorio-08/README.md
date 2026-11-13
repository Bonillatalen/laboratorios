# Laboratorio 08 — Autenticación, sesiones y permisos

Esta entrega agrega autenticación de usuarios, sesiones, dashboard privado y control de acceso por permisos para la revisión del catálogo.

## Funcionalidades

- Registro de usuarios con `UserCreationForm`.
- Login y logout seguro mediante las vistas integradas de Django.
- Dashboard protegido con `@login_required`.
- Contador de visitas almacenado en sesión.
- Resumen privado de recursos.
- Grupo `Catalog reviewers` con permiso `pages.view_resource`.
- Respuesta `302` para usuarios anónimos y `403` para usuarios autenticados sin permiso.

## Pruebas

```bash
python manage.py test pages
```

La suite incluye las pruebas de páginas base, autenticación, sesiones y permisos de revisión del catálogo.
