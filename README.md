# base-docker-django-user-api
This project allows to store your book list and manage them
## Tech Stack

**Core Tech:** Python

**Backend Service:** Django, Django Rest Framework

**Code Format:** PEP8 Standart

**Test:** unittest, Flake8

**Database:** Postgresql

**Container:** Docker

## Features

- Test Driven Development
- User Authentication and Management
- Dockerize System

## API Reference

#### Create a new user

```
  POST /api/user/create
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**.  |
| `password` | `string` | **Required**.|
| `name` | `string` | **Required**.|

#### Create authentication token

```
  POST /api/user/token
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**.  |
| `password` | `string` | **Required**.|

#### Get own information

```
  GET /api/user/me
```

| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Token <token>|

## Run Locally

Clone the project

```bash
  git clone https://github.com/koksalkapucuoglu/base-docker-django-user-api.git
```

Go to the project directory

```bash
  cd base-docker-django-user-api
```

Build docker

```bash
  docker-compose build
```

Start the server

```bash
  docker-compose up
```

## Create Django Superuser 

Go to the project directory

```bash
  cd base-docker-django-user-api
```

Run following command for create a new super user
```bash
  docker-compose run app sh -c "python manage.py createsuperuser"
```
Open browser and go to

```bash
  http://127.0.0.1:8000/admin/login/?next=/admin/
```

## Running Tests

Go to the project directory

```bash
  cd base-docker-django-user-api
```

Run following command for unit test and coding style(PEP8) test

```bash
  docker-compose run app sh -c "python manage.py test && flake8"
```


