import json, os

class config:
    def __init__(self, ruta="config.json"):
        self.ruta = "/".join(os.path.abspath(__file__).split("/")[:-1]+[ruta])

    def load(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            return datos
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None

    def setData(self, key, value):
        with open(self.ruta, 'r', encoding='utf-8') as archivo:
            config = json.load(archivo)
            config[key] = value
            json.dump(config, open(archivo, "w"), indent=4)
            return True