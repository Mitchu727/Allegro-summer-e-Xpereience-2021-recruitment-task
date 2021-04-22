import requests
response = requests.get("https://api.github.com/users/Mitchu727")
print(response.json())
print(response.json()['login'])
