# FreeCodeCamp.org fastAPI tutorial

https://youtu.be/0sOvCWFmrtA

This tutorial focuses on creating an API for a social media site. It walks the student through setting up their development environment, setting up a local Postgres database, testing their API with Postman and the built-in Swagger docs, testing using Pytest, and finally deployment to multiple environments.

## Set up environment

### Create a virtual env and pip install requirements

```
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Create .env file for local dev
You'll need to create .env file with the following environment variables and place at the root of your project directory (on the same level as the app directory). This tutorial uses Postgres, so you'll need to set up a Postgres database on your local machine and provide the approriate values below.

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

You can create the `SECRET_KEY` variable on the command line: `openssl rand -hex 32`.

## Start the local server

`uvicorn app.main:app --reload`



