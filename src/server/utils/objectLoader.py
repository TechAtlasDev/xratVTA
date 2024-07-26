import os, json
from .objects import payload
from typing import Union

RUTA_ARCHIVO = "/".join(os.path.abspath(__file__).split("/")[:-1])

def loadJSON(type="dict") -> Union[dict, payload]:
    payloadConfig = ""
    if type is dict:
        payloadConfig = json.load(open(RUTA_ARCHIVO+"/payload.json", "r"))
    else:
        payloadConfig = payload(payloadConfig)
    
    return payloadConfig