# Setting up developer environment for muggle branch of SortingHat

```
git clone https://github.com/chaoss/grimoirelab-sortinghat/
git switch muggle
cd grimoirelab-sortinghat
python3 -m venv my_venv
source my_venv/bin/activate

poetry install

python3 manage.py runserver --settings=config.settings.devel
```
For starting the vue app

```
cd ui
yarn install 
yarn serve
```

**After applying migrations and creating admin user, the errors have been resolved and I could perform operations using sortinghat UI**


![photos](https://github.com/rohanreddych/chaoss-microtasks/blob/main/photos/4ui.png)

![photos](photos/4server.png)


![photos](photos/4.png)
