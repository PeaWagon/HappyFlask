# Introduction

This is a hackathon boilerplate for new Flask web applications created by [Major League Hacking](https://github.com/MLH). It is for hackers looking to get started quickly on a new hackathon project using the Flask microframework.

- [Installation Guide](#installation-guide) - How to get started with a new Flask app
- [User Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md) - How to develop apps created with this starter project
- [Contributing Guide](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/CONTRIBUTING.md) - How to contribute to the project

# <a name='installation-guide'>Installation Guide</a>

1. Fork and clone the repository or simply clone it from the MLH github page.

    ```bash
    git clone https://github.com/MLH/mlh-hackathon-flask-starter.git
    cd mlh-hackathon-flask-starter
    ```

2. Install [miniconda3] (https://docs.conda.io/en/latest/miniconda.html). Download and run the `.sh` installer as `sudo`.
3. Create a Conda environment with Python 3.6. NOTE: Python 3.8 **will not build** with the given list of dependencies.

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

## Getting Started

**Create an app on GitHub**

Head over to [GitHub OAuth apps](https://github.com/settings/developers) and create a new OAuth app. Name it what you like but you'll need to specify a callback URL, which should be something like: `http://localhost:5000/auth/callback/github`. 

I used the access url as: `http://localhost:5000/`.

The default port for Flask apps is `5000`, but you may need to update this if your setup uses a different port or if you're hosting your app somewhere besides your local machine.

**Setup the Postgres database**

```bash
sudo -i -u postgres
psql
create database happyflask;
\q
exit
```

You need to be able to connect to a database either on your own computer (locally) or through a hosted database. You can [install Postgres locally](http://www.postgresqltutorial.com/install-postgresql/) and [connect to it](http://www.postgresqltutorial.com/connect-to-postgresql-database/) to provide the database for your app.

You will need to know the connection URL for your application which we will call `DATABASE_URL` in your environment variables. Here is an example:

```
postgresql://localhost:5432/mlh-hackathon-starter-flask
```

**Step 5: Update environment variables and run the Server.**

Create a new file named `.env` by duplicating `.env.example`. Update the new file with the GitHub credentials. It should look similar to this:

```
# .env file
DATABASE_URL="[INSERT_DATABASE_URL]"
GITHUB_CLIENT_ID="[INSERT_CLIENT_ID]"
GITHUB_CLIENT_SECRET="[INSERT_CLIENT_SECRET]"
```

You replace the GitHub credentials here and update the database URL. Learn more about the required [Environment Variables here](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md#environment-variables).

Now we're ready to start our server which is as simple as:

```
(venv) $ flask run
```

Open http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

# What's Included?

- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - A Flask extension for making modular applications
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - A Flask extension that adds ORM support for your data models.
- [Werkzeug](http://werkzeug.pocoo.org/) - A Flask framework that implements WSGI for handling requests.
- [Bootstrap 4](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.

# License

The Hackathon Starter Kit is open source software [licensed as MIT](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/LICENSE.md).
