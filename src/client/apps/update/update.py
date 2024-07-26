import git, requests
#from ..utils.loadConfig import load
import sys, os

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
