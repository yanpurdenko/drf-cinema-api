# Cinema API

API service for cinema management written on DRF


## Features

- JWT authenticated
- Admin panel /admin/
- Documentation is located at /api/doc/swagger/
- Managing orders and tickets
- Creating movies with genres, actors
- Creating cinema halls
- Adding movie sessions
- Filtering movies and movie sessions
- Docker app starts only when db is available ( custom command via management/commands )

## Installing using GitHub

1. Install PostgresSQL and create db
2. Copy this repository, by using your terminal:

```shell
git clone https://github.com/yanpurdenko/drf-cinema-api.git
```
3. Change directory
```shell
cd drf-cinema-api
```
4. Install venv, and activate it by using following commands:
```shell
python -m venv venv
```
to activate on Mac and Linux:
```shell
source venv/bin/activate
```
to activate on Windows:
```shell
venv\Scripts\activate
```
5. Install dependencies (requirements):
```shell
pip install -r requirements.txt
```
6. Create file .env and change environment variables to yours as in .env.sample.


7. Run migrations to initialize database. Use this command:
```shell
python manage.py migrate
```
8. Run server
```shell
python manage.py runserver
```


## Run with docker

Docker should be installed

```shell
docker-compose build
docker-compose up
```
Alos use http://127.0.0.1:8000/ url instead of http://0.0.0.0:8000/


## Getting access

- create user via /api/user/register/
- get access token via /api/user/token/


## How to try it out
1. When you received access token, authorize with it on /api/doc/swagger/ and execute all endpoints
2. Or you can install ModHeader extension in Google Chrome and create request header with value Bearer `<Your access token>`
