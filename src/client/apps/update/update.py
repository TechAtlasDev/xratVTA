import git, requests
from ..utils.loadConfig import load

def git_pull(repo_path="../.."):
    print ("Actualizando...")
    repo = git.Repo(repo_path)
    origin = repo.remotes.origin
    origin.pull()

def forUpdate(owner, project, local_path="../.."):
    local = str(git.Repo(local_path).head.commit.hexsha)
    remoto = str(requests.get(f"https://api.github.com/repos/{owner}/{project}/commits").json()[0]["sha"])

    return not (str(local) == str(remoto))
