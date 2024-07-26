import traceback
import socket, json
from utils import objectLoader
import threading
import git, requests
import sys, os
import time

HOST = '0.0.0.0'
PORT = 7788


def git_pull(repo_path="../.."):
    repo = git.Repo(repo_path)
    repo.git.reset('--hard')
    origin = repo.remotes.origin
    origin.pull()

    # Volviendo a ejecutar el script de manera automatica y cerrando el actual
    argumentos = sys.argv[:]
    os.execv(sys.executable, [sys.executable] + argumentos)

def forUpdate(owner, project, local_path="../.."):
    local = str(git.Repo(local_path).head.commit.hexsha)
    remoto = str(requests.get(f"https://api.github.com/repos/{owner}/{project}/commits").json()[0]["sha"])

    return not (str(local) == str(remoto))

def control_update():
    while True:
        if forUpdate("TechAtlasDev", "xratVTA"):
            git_pull()
        time.sleep(1800)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

# Parámetros para la función periódica
param1 = "parámetro1"
param2 = "parámetro2"

# Crear y arrancar el hilo para la tarea periódica con parámetros
task_thread = threading.Thread(target=control_update, daemon=True)
task_thread.start()

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
                    print(repr(data))

    except Exception as Error:
        print(f"[ERROR] {Error}")
        traceback.print_exc()
        server.close()
        break

    except KeyboardInterrupt:
        print('\nServer stopped by user')
        server.close()
        break
