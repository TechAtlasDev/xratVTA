from apps.utils.objects import payload
import socket
from apps.web import web
from apps.update import update
from apps.utils.loadConfig import load

def responder(client, mensaje):
    client.sendall(mensaje.encode())

def processor(client:socket.socket, data:payload):
    
    NAME_PAYLOAD = data.executor.name
    CONFIG = load()
    
    # -- Controlando el payload
    if NAME_PAYLOAD == "web":
        response = web.recv(data)
        responder(client, response.status_code.__str__())

    if NAME_PAYLOAD == "update":
        if update.forUpdate("TechAtlasDev", "xratVTA", "../..") and not CONFIG["dev"]:
            update.git_pull()
        responder(client, "Sistema actualizado")
