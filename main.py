from fastapi import FastAPI
from GithubUserReposInfo import GithubUserReposInfo

app = FastAPI()


@app.get("/")
def root():
    return "Repository browser"


@app.get("/{login}")
def get_user(login):
    GithubUserReposInfo(login)
    return {"Informacje dla użytkownika": login}


@app.get("/{login}/repos")
def list_repos(login):
    user = GithubUserReposInfo(login)
    return user.list_repos()


@app.get("/{login}/stars")
def stars_number(login):
    user = GithubUserReposInfo(login)
    return {user.get_stars_number()}
