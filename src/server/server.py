import traceback
import socket, json
from utils import objectLoader

HOST = '0.0.0.0'
PORT = 50007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    try:
        conn, addr = server.accept()  # -- RECIBIENDO UNA CONEXIÓN
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                payload = objectLoader.loadJSON(dict)
                response_json = json.dumps(payload)
                if data.decode('utf-8') == "get":
                    conn.sendall(response_json.encode('utf-8'))
                else:
                    print (repr(data))

    except Exception as Error:
        print (f"[ERROR] {Error}")
        traceback.print_exc()
        server.close()
        break

    except KeyboardInterrupt:
        print('\nServer stopped by user')
        server.close()
        break

