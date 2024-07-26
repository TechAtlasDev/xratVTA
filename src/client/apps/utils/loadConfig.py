import json, os

def load(ruta="config.json"):
    RUTA_ARCHIVO = "/".join(os.path.abspath(__file__).split("/")[:-1]+[ruta])
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

