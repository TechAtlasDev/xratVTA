from ..utils.objects import payload

# IMPORTANDO LOS METODOS DISPONIBLES
from .executorWeb import *

def recv(data:payload):

    METODO = data.executor.postdata["method"]
    URL = data.executor.execution
    PARAMS = data.executor.postdata["params"]

    if METODO == "get":
        return visitGet(URL, params=PARAMS)

    if METODO == "post":
        return visitPost(URL, params=PARAMS)

