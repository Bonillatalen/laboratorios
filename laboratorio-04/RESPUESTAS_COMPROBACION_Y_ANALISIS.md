# Respuestas a las Preguntas de Comprobación y Análisis

## Comprobación Práctica 4.1
- **Cuándo usar `try/except` vs `if`:** `if` se utiliza para control de flujo y lógica de negocio predecible (como comprobar si un saldo es suficiente o si un número es menor que cero). `try/except` se emplea para situaciones excepcionales o imprevisibles en el entorno de ejecución, como fallas de conversión de tipos (`ValueError`), operaciones de E/S (`FileNotFoundError`) o errores que escapan a la precondición inmediata del código.
- **Qué hace `raise`:** Interrumpe deliberadamente el flujo de ejecución normal lanzando una excepción específica para comunicar que se ha violado un contrato o regla de negocio.
- **Para qué sirve `else`:** Ejecuta un bloque de instrucciones únicamente si el bloque `try` finalizó sin lanzar ninguna excepción.
- **Comportamiento de `finally`:** Garantiza la ejecución de su bloque de código sin importar si ocurrió una excepción o si la función ejecutó un `return`, siendo clave para liberación de recursos externos.
- **No dejar datos parcialmente modificados:** Modificar un atributo antes de validar otros parámetros deja el objeto en un estado corrupto o inconsistente en caso de que ocurra una falla intermedia.

## Comprobación Práctica 4.2
- **Sobrescribir vs Agregar:** El modo `"w"` trunca y reemplaza el archivo por completo; el modo `"a"` posiciona el puntero al final para anexar información sin tocar lo existente.
- **Por qué usar `with`:** Actúa como un gestor de contexto (`context manager`) que asegura la invocación automática del método `.close()` sobre el descriptor de archivo, incluso ante excepciones no controladas.
- **Falta de archivo de lectura:** `open(..., "r")` o `Path.read_text()` disparan un error `FileNotFoundError` que interrumpe la ejecución si no se captura.
- **Propósito de `encoding="utf-8"`:** Estandariza la codificación de caracteres multilingües (tildes, eñes, símbolos) evitando fallos de decodificación multiplataforma (`UnicodeDecodeError`).
- **Rutas con la ubicación del módulo (`__file__`):** Permite calcular la ruta absoluta relativa al archivo fuente con `Path(__file__).resolve().parent`, evitando fallos cuando la terminal se ejecuta desde un directorio raíz distinto.

## Comprobación Práctica 4.3
- **Por qué `json.dump` falla con clases propias:** El serializador por defecto de Python solo maneja tipos primitivos compatibles con la especificación JSON (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`).
- **Conversión y reconstrucción de objetos:** Se implementa un método de instancia `a_diccionario(self)` para extraer un diccionario primitivo y un método de clase `@classmethod desde_diccionario(cls, datos)` que invoca el constructor pasando por todas las validaciones de negocio.
- **Archivo inexistente vs JSON dañado:** La inexistencia indica un estado de inicialización limpia (inventario nuevo); un archivo existente pero mal formado (`JSONDecodeError`) denota corrupción de datos donde sobrescribir equivaldría a pérdida definitiva de información.
- **JSON como persistencia y CSV como reporte:** JSON modela la estructura y tipos nativos necesarios para la reconstrucción de objetos; CSV es un formato plano enfocado en interoperabilidad con hojas de cálculo y análisis tabular.

## Comprobación Práctica 4.4
- **Significado de heredar:** Mecanismo mediante el cual una subclase adquiere atributos y métodos de una superclase, modelando una relación de especialización ("es un tipo de").
- **Función de `super()`:** Permite acceder y delegar comportamiento a la superclase, como invocar su método constructor `__init__`.
- **Sobrescritura de métodos:** Redefinición de la implementación de un método en la subclase manteniendo el mismo nombre o firma que en la clase padre.
- **Reconocimiento del polimorfismo:** Se produce cuando un mismo mensaje o llamada a método (ej. `notificacion.enviar()`) es invocado sobre distintos objetos produciendo comportamientos específicos según la clase receptora, sin depender de estructuras condicionales `if/elif`.
- **Por qué el inventario usa composición:** Un inventario *contiene* productos (relación "tiene un"), no *es* un producto. La composición favorece el bajo acoplamiento y la flexibilidad estructural sin jerarquías rígidas.

---

# Solución a las Preguntas de Análisis Situacional (Informe PDF)

## Pregunta 1: Cierre inesperado y productos desaparecidos
- **Qué haría:** Verificaría de inmediato el estado del archivo `datos/productos.json` y la consola de ejecución.
- **Por qué:** Si el programa se detuvo abruptamente, los cambios pudieron residir exclusivamente en la memoria RAM si no se invocó la función de persistencia antes del fallo o si la ruta de guardado apuntó a una carpeta diferente a la de lectura.
- **Cómo implementarlo:** Inspeccionar `almacenamiento.py` para asegurar que las rutas se construyan siempre de forma anclada al script:
  ```python
  BASE_DIR = Path(__file__).resolve().parent
  RUTA_JSON = BASE_DIR / "datos" / "productos.json"
  ```
  Asimismo, implementar un guardado inmediato tras cada mutación exitosa en `main.py` y asegurar que `main.py` invoque `guardar_inventario()` al salir.
- **Comprobación:** Registrar productos, forzar el cierre de la terminal, reabrir y comprobar la salida de la opción 2 (Listar productos), verificando que los datos coincidan con el contenido del archivo físico `productos.json`.

## Pregunta 2: Archivo `productos.json` existente pero con sintaxis rota (coma faltante)
- **Qué haría:** Interceptar `json.JSONDecodeError` al iniciar el programa, emitir una alerta en consola y bloquear las operaciones que sobrescriban el archivo en disco, pasando la aplicación a un modo de contingencia o solo lectura.
- **Por qué:** Tratar el error como una lista vacía y ejecutar un nuevo guardado provocaría que el archivo dañado (pero potencialmente recuperable mediante edición manual) sea destruido y reemplazado por `[]`.
- **Cómo implementarlo:** En `almacenamiento.py`:
  ```python
  try:
      with RUTA_JSON.open("r", encoding="utf-8") as f:
          datos = json.load(f)
      inventario.cargar_desde_lista_diccionarios(datos)
      return inventario, None
  except json.JSONDecodeError as err:
      return None, f"Error de formato JSON: {err}"
  ```
- **Comprobación:** Introducir intencionalmente una coma faltante en `productos.json`, arrancar la aplicación, confirmar que se imprima la advertencia sin alterar el archivo y luego corregir la coma manualmente para confirmar que el inventario vuelva a cargar los registros.

## Pregunta 3: Códigos duplicados detectados al recuperar el JSON
- **Qué haría:** Centralizar la validación de unicidad en la clase `Inventario` y aplicar un enfoque atómico de carga utilizando una instancia temporal.
- **Por qué:** Si la validación falla a mitad de la lectura, un proceso de carga directo dejaría el inventario en un estado parcialmente poblado e inconsistente.
- **Cómo implementarlo:** En `inventario.py`, cargar primero en una colección auxiliar; si algún registro repite código, la validación lanzará `ValueError` y el inventario activo mantendrá su estado anterior sin corromperse:
  ```python
  def cargar_desde_lista_diccionarios(self, lista_datos):
      temp = Inventario()
      for d in lista_datos:
          prod = Producto.desde_diccionario(d)
          temp.agregar_producto(prod)  # Lanza ValueError si está repetido
      self._productos = temp._productos
  ```
- **Comprobación:** Crear manualmente un JSON con dos registros con código `"P001"`. Ejecutar el sistema y verificar que se rechace la carga total notificando la inconsistencia sin agregar el primer registro a la colección activa.

## Pregunta 4: CSV calcula precio unitario en vez de valor total
- **Qué haría:** Corregir la asignación del campo `valor_inventario` en `reportes.py`.
- **Por qué:** Las responsabilidades de consolidación tabular y reportes residen en `reportes.py`. Escribir únicamente `p.precio` en la columna analítica es un error aritmético de exportación.
- **Cómo implementarlo:** Ajustar la generación de la fila en `reportes.py`:
  ```python
  filas.append({
      "codigo": p.codigo,
      "nombre": p.nombre,
      "categoria": p.categoria,
      "precio": p.precio,
      "cantidad": p.cantidad,
      "valor_inventario": p.precio * p.cantidad  # Cálculo correcto
  })
  ```
- **Comprobación:** Tomar un producto con precio $45,000 y cantidad 5. Exportar el CSV y abrir el archivo `reportes/inventario.csv` para verificar que la columna `valor_inventario` muestre exactamente `225000.0`.

## Pregunta 5: Regresión en la carga tras modificar el guardado
- **Qué haría:** Usar las herramientas de trazabilidad de Git para comparar los cambios entre commits (`git diff`), aislar el fallo y aplicar una prueba de regresión.
- **Por qué:** En arquitecturas modulares, alterar los nombres de las claves del diccionario serializado en `guardar_inventario` (por ejemplo, cambiar `"codigo"` por `"cod"`) rompe la deserialización en `desde_diccionario()`.
- **Cómo implementarlo:**
  1. Identificar el último commit funcional: `git log --oneline`.
  2. Ejecutar `git diff <hash_anterior> <hash_actual>` para examinar las discrepancias introducidas en `a_diccionario` o en la rutina de escritura.
  3. Corregir la estructura del payload para restablecer la paridad contractual entre el serializador y el constructor.
  4. Generar un commit descriptivo de la corrección: `git commit -m "fix: corregir discrepancia de claves serializables en almacenamiento"`.
- **Comprobación:** Ejecutar un flujo de prueba completo: registrar datos, guardar con la función modificada, reiniciar la aplicación y validar que la deserialización procese la totalidad de los objetos sin arrojar excepciones `KeyError`.
