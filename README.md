Setup and activate a virtualenv

```
$ mkdir venv
$ cd venv
$ virtualenv -p python3 alchemy
$ source alchemy/bin/activate
```

Clone repository

```
$ git clone
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
