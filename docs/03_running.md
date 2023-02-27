---
layout: default
title: Running the API locally
nav_order: 3
description: "How to start the server and view the docs"
permalink: /running_the_api
---

# Running this API locally
{: .fs-9}

Instructions for running this API on your local machine.
{: .fs-6 .fw-300 }

If you want to clone the [repo](https://github.com/rtreddick/fcc-fastapi) and run this API locally, you can follow the instructions below to set up your environment and start the uvicorn server. When the server starts, it will display the path to the server running on local host. Visit the path *ip-address*/docs to view the built in Swagger docs.

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
```
. venv/bin/activate
uvicorn app.main:app --reload`
```


