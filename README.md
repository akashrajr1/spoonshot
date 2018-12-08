# Movie Manager
A simple movie manager   
## Setting up the server
- Install python packages 
```
sudo pip install -r requirements.txt
```
- Running through tmux  
  Common commands for navigation 
  * `tmux list-sessions` Lists all sessions
  * `tmux` Start session
  * `Cntrl+B D` Break and detach session
  * `tmux attach -tn` n is the session id you want to join
A more comprehensive guide is available at  
https://www.linkedin.com/pulse/how-i-run-days-long-scripts-without-breaking-them-arun-das/  
https://gist.github.com/MohamedAlaa/2961058  
## Code Guide
For more details reference the comments within the code. They have been grouped in commits for convenience 
* html comments https://github.com/akashrajr1/spoonshot/commit/cb99531a6a6f924efea66316283ceda2cb24f701
* py comments https://github.com/akashrajr1/spoonshot/commit/d6d3d7885300dc3c9fc9a3841404328f6198f7da
## Deployment Guide
Changes to be made in the `/moviemanger/settings.py` 
* The public facing ip must be mentioned in the `ALLOWED_HOSTS`
Current configuration  
```
ALLOWED_HOSTS = ['159.89.169.62','spoonshot.ml']
```
* Static files like images and css are stored in the `STATIC_URL`
## Assumptions Made
1. Though the API mentioned details like Primary Info, Alternative titles, etc. the actual API didnt provide these details and hence only the details which were made available were used. They are:
   * Original Title
   * Tagline
   * Summary
   * Homepage
   * Language
   * Revenue
   * Release Date
   * Runtime
   * Rating  
  
2. The search module has been currently set as the default page, but it can be moved to /search url by removing line 21 in [spoonshot/moviemanager/urls.py](https://github.com/akashrajr1/spoonshot/blob/master/moviemanager/urls.py) ie.
`    url(r'^', include('search.urls')),`
3. To enhance security a simple csrf token has been added for the form to prevent cross site request forgery
4. Additional modules like /book can be added as all modules are independent
## Frontend
- Search Page
![](https://github.com/akashrajr1/spoonshot/blob/master/search.JPG)
- Details Page
![](https://github.com/akashrajr1/spoonshot/blob/master/details.JPG)
