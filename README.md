Setup and activate a virtualenv

```
$ mkdir venv
$ cd venv
$ virtualenv -p python3 alchemy
$ source alchemy/bin/activate
```

Clone repository

```
$ git clone git@github.com:phroiland/homework.git or https://github.com/phroiland/homework.git
$ cd homework
```
Install requirements

```
$ pip install -r requirements.txt
```

Run Migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create Admin Superuser
```
$ python manage.py createsuperuser
```
Runserver
```
$ python manage.py runserver
```


<h2>TODO</h2>
* endpoints need to be refactored and redundancy needs to be removed to match gist. (i.e., register is under login)
* files can upload but unable to actually view. 
* django is recogninzing subsequent file uploads as already having been uploaded by the user--regardless of the file name.
