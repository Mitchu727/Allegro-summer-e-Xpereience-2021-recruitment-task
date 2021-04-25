# Allegro-summer-e-Xpereience-2021-recruitment-task
Server app created as a recruitment task for [Allegro](https://about.allegro.eu/).
## Task number - 3
## Installation and set up
To run this app you should have *fastapi*, *uvicorn* and *requests* libraries installed. To install them run:

`pip install fastapi requests uvicorn`

To launch server run in repository directory:

`uvicorn main:app --reload`

Now you can go to http://127.0.0.1:8000 in your browser and see the response of the server!
Typing in http://127.0.0.1:8000/username will show you information whether the user with `username` exists.  
for example:  
http://127.0.0.1:8000/Mitchu727 

To list his repos you should use: http://127.0.0.1:8000/username/repos  
for example:  
http://127.0.0.1:8000/Mitchu727/repos

To count stars in all of users repos you should use: http://127.0.0.1:8000/username/stars  
for example:  
http://127.0.0.1:8000/Mitchu727/stars
## Notes
First issues was that, at the one stage of the project a decision was needed to make whether it would be better to story information about repos in an object or making request every time. I've decided to the second solution due to the task requirements and fastapi architecture.  
Second issue was the case of the loading data about repos. At first they were loaded during the initialization of the GithubUserReposInfo object (by the way the existence of the user would also be checked) but later I've decided to implement a method that checks whether the user exists separately and have placed it in the constructor. Data is loaded before a method that counts stars or list repos. This solution would be better if one's creating a list of this objects for the later use and it also makes the app easier to extend.
## Further improvements
### Optimalization
To optimize the app and make it more flexible, it would be more convenient to store some data about repos in the memory  with the information when it was updated for the last time. If the timespan between this moment and the present moment would be bigger than given value, data will be updated.
### Frontend
It would be good to make some GUI for the app so it would be more convenient to use and more readable.
### Analysis
Some simple methods can be written that would extract more data from the api and could be use in an analysis. For example one can analyse the relation between stars count and user activity or compare if repos with "nutella" in the name have more stars than the average.