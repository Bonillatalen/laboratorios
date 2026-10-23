# Gestor de inventario orientado a objetos

## Descripción

En este proyecto transformé el gestor procedural del Laboratorio 02 en una aplicación orientada a objetos. La interacción con la persona usuaria queda en `main.py`, mientras que las clases se encargan de los datos y las operaciones.

## Módulos

- `producto.py`: contiene la clase `Producto`, sus atributos privados, propiedades, validaciones y métodos `actualizar_existencias()` y `calcular_valor()`.
- `inventario.py`: contiene la clase `Inventario`, que maneja su propia lista de objetos `Producto`. Incluye registro, búsqueda, listado, actualización, eliminación y resumen.
- `main.py`: muestra el menú y solicita los datos mediante `input()`. No contiene la lógica interna de las clases.
- `test_poo.py`: comprueba propiedades, validaciones, operaciones, informes y la independencia entre dos inventarios.
- `pruebas_independencia.py`: demuestra que dos inventarios no comparten la lista de productos.

## Ejecución

Desde esta carpeta:

```bash
python3 main.py
python3 -m unittest discover -s . -p 'test*.py' -v
python3 pruebas_independencia.py
```

Las categorías permitidas son `Periféricos`, `Componentes`, `Accesorios` y `Oficina`. El precio debe ser mayor que cero y la cantidad debe ser cero o positiva.
