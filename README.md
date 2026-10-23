# Laboratorios de Python



Repositorio personal de **Karen Sirley Bonilla Ramirez** (ficha **3388087**) para organizar las actividades de los laboratorios de Python.



## Estructura



```text

laboratorios/

├── README.md

├── laboratorio-01/

│   ├── ejercicios de fundamentos

│   ├── cotizador_compra.py

│   └── pruebas/

└── laboratorio-02/

    ├── ejercicios de control y colecciones

    ├── gestor_inventario.py

    └── pruebas/

```



Los archivos del Laboratorio 01 se conservaron sin reemplazarlos. El Laboratorio 02 se agregó en una carpeta independiente.



## Laboratorio 01



Incluye ejercicios sobre variables, tipos de datos, operadores y entrada de información, además del cotizador de compras.



```bash

python3 laboratorio-01/cotizador_compra.py

cd laboratorio-01

python3 -m unittest discover -s pruebas -v

```



## Laboratorio 02



Incluye ejercicios sobre estructuras de control, listas, tuplas, conjuntos, diccionarios, comprensiones y operaciones de inventario. El gestor permite registrar, consultar, buscar, actualizar y eliminar productos.



```bash

python3 laboratorio-02/gestor_inventario.py

cd laboratorio-02

python3 -m unittest discover -s pruebas -v

```



El gestor acepta las categorías `Periféricos`, `Componentes`, `Accesorios` y `Oficina`. Los códigos deben ser únicos, los precios deben ser positivos y las cantidades no pueden ser negativas.



## Requisitos



Python 3.8 o posterior. No se necesitan dependencias externas.

