import requests


class GithubUserInfo():
    def __init__(self, name):
        self.name = name
        self.refresh()

    def refresh(self):
        self.response = requests.get("https://api.github.com/users/" + self.name)


TestUser = GithubUserInfo("Mitchu727")
print(TestUser.response.json())
print(TestUser.response.json()['login'])
