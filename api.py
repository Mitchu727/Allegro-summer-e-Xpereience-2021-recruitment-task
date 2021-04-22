import requests


class GithubUserInfo():
    def __init__(self, name):
        self.name = name
        self.refresh()

    def refresh(self):
        self.response = requests.get("https://api.github.com/users/" + self.name)
        self.repos = requests.get(self.response.json()['repos_url'])

    def get_repos(self):
        return self.repos

    def list_repos(self):
        for repo in self.repos.json():
            print(repo['name'])


TestUser = GithubUserInfo("Mitchu727")
TestUser.list_repos()
# print(TestUser.get_repos().json()[0]['name'])
# print(TestUser.response.json()['login'])
