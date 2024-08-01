# Clase que se ejecuta cuando hay un error, y se busca recuperar el acceso a través de actualizaciones
from ..utils import handleExceptions
import git, requests
import sys, os, socket

# MÉTODO DE RECUPERACIÓN
"""ESTE MÉTODO CONSISTE EN CONSUMIR LA MENOR CANTIDAD DE RECURSOS, Y CADA VEZ QUE SE EJECUTE
SE VA A INTENTAR ENVIAR INFORMACIÓN DE LA EXCEPCIÓN CAPTURADA AL SERVIDOR PRINCIPAL, Y
ADEMÁS, SE VA A BUSCAR ACTUALIZACIONES DEL REPOSITORIO"""

class recovery():
    def __init__(self, error:Exception) -> None:

        responseServer = requests.get("https://varlives.vercel.app/?key=ipVPS").json()

        self.INFO_AUX = {
            "ip": responseServer["value"],
            "port": responseServer["port"],
            "owner": "TechAtlasDev",
            "project": "xratVTA",
        }
        self.error = error
    
    def git_pull(self, repo_path="../.."):
        try:
            repo = git.Repo(repo_path)
            repo.git.reset('--hard')
            origin = repo.remotes.origin
            origin.pull()

            # Volviendo a ejecutar el script de manera automatica y cerrando el actual
            argumentos = sys.argv[:]
            os.execv(sys.executable, [sys.executable] + argumentos)

        except:
            return False

    def forUpdate(self):
        try:
            local = str(git.Repo("../..").head.commit.hexsha)
            remoto = str(requests.get(f"https://api.github.com/repos/{self.INFO_AUX['owner']}/{self.INFO_AUX['project']}/commits").json()[0]["sha"])

            return not (str(local) == str(remoto))
        except:
            return True

    def sendError(self):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.INFO_AUX["ip"], self.INFO_AUX["port"]))

            MENSAJE = handleExceptions.handle(self.error).__str__()

            client.sendall(MENSAJE.encode())
            return True
        except:
            return False