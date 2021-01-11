# Introduction

HappyFlask is a hackathon project built for the purpose of learning about Flask and Python web development.

## Installation Guide

These instructions aim to be more specific than those provide with the original boilerplate. These instructions were used for installing and setting up the website on Ubuntu 20.04.1 LTS.

### Install the dependencies

1. Fork and clone the repository or simply clone it from the MLH github page.

    ```bash
    git clone https://github.com/MLH/mlh-hackathon-flask-starter.git
    cd mlh-hackathon-flask-starter
    ```

2. Install [miniconda3](https://docs.conda.io/en/latest/miniconda.html). Download and run the `.sh` installer as `sudo`.
3. Create and activate a Conda environment with Python 3.6. NOTE: Python 3.8 **will not build** with the given list of dependencies.

    ```bash
    conda create -n hackenv python=3.6
    conda activate hackenv
    ```

4. Install the Python dependencies, located in `requirements.txt`. Make sure the correct `pip` is being used to install the dependencies.

    ```bash
    which pip            
    ~/.conda/envs/hackenv/bin/pip
    pip install -r requirements.txt
    ```

5. Install PostgreSQL.

    ```bash
    sudo apt install postgresql
    ```

6. Check that the Postgres service has started, otherwise start it up.

    ```bash
    systemctl status postgresql.service
    sudo systemctl start postgresql.service
    ```

### Setup the Postgres database

```bash
sudo -i -u postgres
psql
CREATE DATABASE happyflask;
CREATE USER test;
ALTER USER test WITH ENCRYPTED PASSWORD 'password-goes-here';
\q
exit
```

You need to be able to connect to a database either on your own computer (locally) or through a hosted database. You can [install Postgres locally](http://www.postgresqltutorial.com/install-postgresql/) and [connect to it](http://www.postgresqltutorial.com/connect-to-postgresql-database/) to provide the database for your app.

You will need to know the connection URL for your application which we will call `DATABASE_URL` in your environment variables. Here is an example:

```bash
postgresql://localhost:5432/happyflask
```

Note: to get the connection working, I needed to create a new user and add their authentication to my `.env` file. Here is the format that worked:

```bash
postgresql://user:password@localhost:5432/database_name
```

### Create an OAuth App on GitHub

Note: the default port for Flask apps is `5000`. Make sure to update the port when outside of localhost.

1. Go to [GitHub OAuth apps](https://github.com/settings/developers) and create a new OAuth app.
2. Choose a name for the app.
3. Specify a Homepage URL (the access point for the app). I used the access URL: `http://localhost:5000/`.
4. Specify a callback URL: `http://localhost:5000/auth/callback/github`.
5. A Client ID should be visible for the OAuth App. Click the `Generate a new client secret` button to generate the respective client secret key and copy it to the clipboard. Leave the browser window open until the next steps are completed to avoid losing access to the secret key.

### Update environment variables and run the server

1. Make a copy of `.env.example` called `.env`.
2. Update the `.env` file with the GitHub credentials:

    ```bash
    DATABASE_URL="[INSERT_DATABASE_URL]"
    GITHUB_CLIENT_ID="[INSERT_CLIENT_ID]"
    GITHUB_CLIENT_SECRET="[INSERT_CLIENT_SECRET]"
    ```

    You replace the GitHub credentials here and update the database URL. Learn more about the required [Environment Variables here](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md#environment-variables).

3. Start the development server:

    ```bash
    flask run
    ```

4. Open (http://localhost:5000)[] to view it in your browser. The app will automatically reload if you make changes to the code. You will see the build errors and warnings in the console.

## Acknowledgements & License

HappyFlask is a hackathon project built using the boilerplate for new Flask web applications created by [Major League Hacking](https://github.com/MLH).

The Hackathon Starter Kit is open source software [licensed as MIT](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/LICENSE.md).

- [User Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md) - How to develop apps created with this starter project
- [Contributing Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/CONTRIBUTING.md) - How to contribute to the project
