# Laboratorio 02 — Estructuras de control y colecciones

**Aprendiz:** Karen Sirley Bonilla Ramirez  
**Ficha:** 3388087

## Descripción

En esta carpeta conservé los ejercicios del material sobre condicionales, ciclos, listas, tuplas, conjuntos, diccionarios y comprensiones. También desarrollé `gestor_inventario.py`.

## Gestor de inventario

El gestor trabaja con una lista de diccionarios. Cada producto tiene código, nombre, categoría, precio y cantidad. El menú permite:

1. Registrar productos.
2. Consultar todos los productos.
3. Buscar por código.
4. Actualizar nombre, categoría, precio y cantidad.
5. Eliminar productos.
6. Consultar un informe del inventario.

Las categorías permitidas son `Periféricos`, `Componentes`, `Accesorios` y `Oficina`. El programa rechaza códigos duplicados, categorías diferentes a las permitidas, precios menores o iguales a cero y cantidades negativas.

## Colecciones y estructuras utilizadas

- **Lista:** mantiene los productos durante la ejecución y permite agregar o eliminar registros.
- **Diccionario:** representa los datos de cada producto mediante claves.
- **Conjunto:** obtiene las categorías diferentes sin repetirlas.
- **Comprensiones:** construyen categorías, productos agotados y unidades agrupadas.
- **Condicionales y ciclo `while`:** controlan el menú y las decisiones de cada operación.
- **Ciclo `for`:** recorre productos para buscar, mostrar y calcular informes.

## Ejecución

```bash
python3 gestor_inventario.py
```

Para ejecutar las pruebas:

```bash
cd laboratorio-02
python3 -m unittest discover -s . -p 'pruebas*.py' -v
```

El informe económico usa `precio * cantidad` para cada producto y suma esos valores.
