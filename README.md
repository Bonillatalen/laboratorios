# Laboratorios de Python



Repositorio personal de **Karen Sirley Bonilla Ramirez** (ficha **3388087**) para organizar las actividades de Python.



## Evolución del proyecto



```text

laboratorios/

├── README.md

├── laboratorio-01/  # Fundamentos y cotizador

├── laboratorio-02/  # Control, colecciones y gestor procedural

├── laboratorio-03/  # Funciones, módulos y gestor POO

└── laboratorio-04/  # Persistencia JSON, reportes CSV y excepciones

```



Los laboratorios anteriores se conservaron sin reemplazarlos. Cada etapa muestra la evolución del mismo gestor: primero fundamentos, después colecciones, luego clases y finalmente persistencia en archivos.



## Laboratorio 01



Variables, tipos, operadores, entrada de información y cotizador.



```bash

python3 laboratorio-01/cotizador_compra.py

cd laboratorio-01 && python3 -m unittest discover -s pruebas -v

```



## Laboratorio 02



Estructuras de control, colecciones y gestor procedural.



```bash

python3 laboratorio-02/gestor_inventario.py

cd laboratorio-02 && python3 -m unittest discover -s pruebas -v

```



## Laboratorio 03



Funciones, módulos y transformación del gestor a POO con `Producto`, `Inventario` y `main.py`.



```bash

cd laboratorio-03/gestor_inventario

python3 main.py

python3 -m unittest discover -s . -p 'test*.py' -v

```



## Laboratorio 04



Gestor persistente con JSON, reporte CSV y manejo de excepciones. La aplicación valida los datos antes de guardarlos, recupera el inventario al iniciar, evita sobrescribir un JSON dañado y mantiene separadas las responsabilidades de negocio, almacenamiento, reportes e interacción.



```bash

cd laboratorio-04/gestor_inventario

python3 main.py

python3 -m unittest discover -s . -p 'test*.py' -v

```



Los datos se generan dentro de `laboratorio-04/gestor_inventario/datos` y los reportes dentro de `laboratorio-04/gestor_inventario/reportes`.



## Requisitos



Python 3.8 o posterior. No se necesitan dependencias externas.

