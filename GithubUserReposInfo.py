import requests


class GithubUserReposInfo():
    def __init__(self, login):
        self._login = login
        self.load_repos()

    def load_repos(self):
        self._repos = []
        request = requests.get("https://api.github.com/users/" +
                               self._login + "/repos?per_page=100&page=1")
        page_numerator = 1
        self.check_request(request)
        while (len(request.json()) > 0):
            for repo in request.json():
                self._repos.append(repo)
            page_numerator += 1
            request = requests.get("https://api.github.com/users/" + self._login +
                                   "/repos?per_page=100&page=" + str(page_numerator))

    def get_repos(self):
        return self._repos

    def get_stars_number(self):
        star_number = 0
        for repo in self._repos:
            star_number += repo['stargazers_count']
        return star_number

    def list_repos(self):
        repos_list = []
        for repo in self._repos:
            repos_list.append({repo['name']: repo['stargazers_count']})
        return repos_list

    def check_request(self, request):
        if (request.status_code >= 400):
            raise Exception(request.json()['message'])
