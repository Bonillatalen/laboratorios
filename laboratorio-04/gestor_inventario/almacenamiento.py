"""Persistencia JSON del inventario."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorAlmacenamiento(Exception):
    """Error controlado al guardar o recuperar información."""


def guardar_inventario(inventario, ruta=RUTA_JSON):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    temporal = ruta.with_suffix(ruta.suffix + ".tmp")
    try:
        with temporal.open("w", encoding="utf-8") as archivo:
            json.dump(inventario.exportar_datos(), archivo, ensure_ascii=False, indent=2)
            archivo.write("\n")
        temporal.replace(ruta)
    except (OSError, TypeError, ValueError) as error:
        if temporal.exists():
            temporal.unlink()
        raise ErrorAlmacenamiento(f"No se pudo guardar el inventario: {error}") from error
    return ruta


def cargar_inventario(ruta=RUTA_JSON):
    from inventario import Inventario

    ruta = Path(ruta)
    if not ruta.exists():
        return Inventario()
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return Inventario(datos)
    except (OSError, json.JSONDecodeError, TypeError, ValueError, KeyError) as error:
        # No se devuelve un inventario vacío: el llamador debe decidir cómo proteger datos.
        raise ErrorAlmacenamiento(
            f"No se pudo cargar {ruta.name}; el archivo no fue sobrescrito: {error}"
        ) from error
