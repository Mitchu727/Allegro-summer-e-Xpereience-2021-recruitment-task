from GithubUserReposInfo import GithubUserReposInfo, HTTPException
import pytest
"""
Tests are checking things that are in the github database, 
therefore they are situation-sensitive. This means that they will work for a short period of time, because tested data will change
(f.e. numbers of stargazers of a repository will grow a user, who have not existed before will appear).
"""
TestUser = GithubUserReposInfo("Mitchu727")


def test_stars():
    assert TestUser.get_stars_number() == 0


def test_repos_number():
    assert len(TestUser.get_repos()) == 3


def test_non_existing_user():
    with pytest.raises(HTTPException):
        BadUser = GithubUserReposInfo("MitchuasdsadadasdasdwadsaxXwaxadwaxaxsaxawacascaws727")
