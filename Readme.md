# Project stacks

In this project used python programming language, database postgres and
ubuntu os, so you have to install python and postgres.

## Database

It is best to use postgres tool to build database:

```sh
$ sudo su postgres
$ psql
$ create database database_name;
(by default owner is 'postgres')
$ \l
```

## Git

Clone project from git repo

```sh
$ git clone https://github.com/Nursultanke/tt_it_attractor.git
```
## Building

We are using python `virtualenv` tool to build:

```sh
$ cd tt_it_attractor
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ touch .env
```
put in .env file your own data like in example bellow

```sh
DB = your_db_name
DB_USER = your_db_user_name
DB_PASSWORD = your_db_password
DJANGO_SECRET_KEY = your_django_secret_key
DB_HOST= your_db_host
```
to get django secret key you can use https://djecrety.ir/ this web service

continue building project

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```

##Get data in json format
We are using django rest framework
 
to get list of articles 
http://127.0.0.1:8000/api/articles
to get list of categories
http://127.0.0.1:8000/api/categories
replace http://127.0.0.1:8000 with your host name
