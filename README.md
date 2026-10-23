# Laboratorios de Python



Repositorio personal de **Karen Sirley Bonilla Ramirez** (ficha **3388087**) para organizar las actividades de Python.



## Estructura



```text

laboratorios/

├── README.md

├── laboratorio-01/  # Variables, tipos, operadores, entradas y cotizador

├── laboratorio-02/  # Control, colecciones y gestor procedural

└── laboratorio-03/  # Funciones, módulos y programación orientada a objetos

```



Los laboratorios anteriores se conservaron sin reemplazarlos. Cada actividad nueva está organizada en su propia carpeta.



## Laboratorio 01



Ejercicios de variables, tipos de datos, operadores y entrada de información, además del cotizador.



```bash

python3 laboratorio-01/cotizador_compra.py

cd laboratorio-01

python3 -m unittest discover -s pruebas -v

```



## Laboratorio 02



Ejercicios de estructuras de control y colecciones, junto con el gestor procedural.



```bash

python3 laboratorio-02/gestor_inventario.py

cd laboratorio-02

python3 -m unittest discover -s pruebas -v

```



## Laboratorio 03



Ejercicios de funciones, módulos y POO. El gestor se reorganizó en los módulos `producto.py`, `inventario.py` y `main.py`, separando la interacción de las operaciones de las clases.



```bash

cd laboratorio-03/gestor_inventario

python3 main.py

python3 -m unittest discover -s . -p 'test*.py' -v

```



El gestor orientado a objetos valida códigos, nombres, categorías, precios y cantidades. También demuestra que dos objetos `Inventario` mantienen colecciones independientes.



## Requisitos



Python 3.8 o posterior. No se necesitan dependencias externas.

