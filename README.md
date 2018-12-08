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
