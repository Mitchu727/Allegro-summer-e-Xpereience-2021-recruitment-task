import requests
import json

class GithubUserReposInfo():
    def __init__(self, login):
        self._login = login
        self.load_repos()

    def load_repos(self):
        user_response = requests.get("https://api.github.com/users/" + self._login)
        self._repos_url = user_response.json()['repos_url']
        self._repos = requests.get(self._repos_url)

    def get_repos(self):
        return self._repos

    def get_star_number(self):
        star_number = 0
        for repo in self._repos.json():
            star_number += repo['stargazers_count']
        return star_number

    def list_repos(self):
        repos_list = []
        for repo in self._repos.json():
            repos_list.append({repo['name']: repo['stargazers_count']})
        return repos_list