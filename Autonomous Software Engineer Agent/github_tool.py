from git import Repo

def clone_repo(repo_url):
    Repo.clone_from(repo_url, "cloned_repo")
    return "Repository Cloned Successfully"
