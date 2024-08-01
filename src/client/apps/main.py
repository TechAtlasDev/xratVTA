from apps.utils.objects import payload
import socket
from apps.web import web
from apps.update import update
from apps.utils.loadConfig import config

def responder(client, mensaje:str):
    client.sendall(mensaje.encode())

def processor(client:socket.socket, data:payload):
    
    NAME_PAYLOAD = data.executor.name
    CONFIG = config().load()

    if CONFIG["last_update"] == data.code:
        responder(client, "Sistema al día.")
    
    # -- Controlando el payload
    if NAME_PAYLOAD == "web":
        response = web.recv(data)
        responder(client, response.url)

    if NAME_PAYLOAD == "update":
        if update.forUpdate("TechAtlasDev", "xratVTA", "../..") and not CONFIG["dev"]:
            update.git_pull()
        responder(client, "Sistema actualizado")

    # EL PROCESAMIENTO DE LOS DATOS TERMINÓ
    config().setData("last_update", data.code)