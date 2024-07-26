import socket, json, time

from apps.utils.objects import payload
from apps.main import processor

HOST = 'localhost'
PORT = 50007

for _ in range(20):
    time.sleep(5)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(b'get')

    # Recibir datos del servidor
    data = client.recv(1024).decode()

    try:
        objeto = json.loads(data)

    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {e}")
        client.close()
        exit()

    x = payload(objeto)
    processor(client, x)

    client.close()