from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/{login}")
def list_repos(login):
    return {"login": login}


@app.get("/{login}/repos")
def list_repos(login):
    return {"repos string 1", "repos string 2"}
