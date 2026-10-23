# Gestor de inventario persistente

## Descripción

Esta es la evolución del gestor orientado a objetos del Laboratorio 03. Ahora conserva los productos en JSON y permite exportar un reporte CSV.

## Responsabilidades

- `producto.py`: clase `Producto`, propiedades, validaciones y serialización.
- `inventario.py`: reglas del negocio, colección de productos, operaciones CRUD y resumen.
- `almacenamiento.py`: lectura y escritura JSON. Usa escritura atómica y nunca reemplaza un archivo dañado por una lista vacía.
- `reportes.py`: exportación del inventario a CSV con el valor calculado como precio por cantidad.
- `main.py`: menú, entradas del usuario y manejo de excepciones.
- `test_persistencia.py`: pruebas de recuperación, JSON inválido, duplicados, valores negativos y CSV.

## Ejecución

Desde `laboratorio-04/gestor_inventario`:

```bash
python3 main.py
python3 -m unittest discover -s . -p 'test*.py' -v
```

Al iniciar, el programa recupera `datos/productos.json` si existe. Si el archivo está dañado o contiene productos inválidos, muestra un error y no lo sobrescribe automáticamente. El reporte se genera en `reportes/inventario.csv`.

## Flujo de persistencia

Cada registro, actualización o eliminación guarda el inventario. Al elegir salir también se guarda. La carga valida todos los registros antes de reemplazar la colección interna, evitando una carga parcial.
