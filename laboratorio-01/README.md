# Laboratorio 01 — Fundamentos de Python

**Aprendiz:** Karen Sirley Bonilla Ramirez  
**Ficha:** 3388087

## Descripción

Esta carpeta conserva los ejercicios de variables, tipos de datos, operadores y entrada de información entregados en el material del laboratorio. También contiene `cotizador_compra.py`, una versión funcional del cotizador de compras.

## Funcionalidades del cotizador

- Solicita datos del cliente, producto, precio unitario y cantidad.
- Solicita porcentajes de descuento e impuesto.
- Calcula subtotal, descuento, base gravable, impuesto, costo de envío y total.
- Valida rangos y valores negativos.
- Maneja entradas no numéricas con un mensaje orientador, sin terminar con un traceback.

La fórmula aplicada es: `total = (subtotal - descuento) + impuesto + envío`, donde el impuesto se calcula sobre la base después del descuento.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 laboratorio-01/cotizador_compra.py
```

Para ejecutar las pruebas automatizadas:

```bash
cd laboratorio-01
python3 -m unittest discover -s pruebas -v
```

## Caso manual de referencia

Con precio unitario `50000`, cantidad `2`, descuento `10 %`, impuesto `19 %` y envío `1000`:

- Subtotal: `$100000.00`
- Descuento: `$10000.00`
- Base después del descuento: `$90000.00`
- Impuesto: `$17100.00`
- Total: `$108100.00`
