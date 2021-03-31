# Setting up dev environment for GrimoireLab

✔️ Setup complete and running.

Steps I followed:

- Download and Install PyCharm IDE.
- Using [this](https://github.com/vchrombie/grimoirelab-scripts/blob/master/glab-dev-env-setup.py) script I cloned the repositories to my local machine.
- Added dependencies like perceval, sortinghat through the Project Structure of the PyCharm IDE. Added dependencies like Flask through project interpreter and pip.
- For docker-compose, we have to increase the virtual memory using `sysctl -w vm.max_map_count=262144`. 


We can get github api token using https://github.com/settings/tokens . 

  
