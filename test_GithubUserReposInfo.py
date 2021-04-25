from GithubUserReposInfo import GithubUserReposInfo
"""
Tests are checking things that are in the github database, 
therefore they are situation-sensitive. This means that they will work for a short period of time, because tested data will change
(f.e. numbers of stargazers of a repository will grow a user, who have not existed before will appear).
"""
TestUser = GithubUserReposInfo("Mitchu727")

def test_stars():
    assert TestUser.get_stars_number() == 0
