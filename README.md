# pfa-backend

Behold My Awesome Project!

This project is a backend application built with Django, designed to manage and facilitate various functionalities for the eLAB platform. It includes user management, data handling, and integration with Docker for easy deployment and development.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.
- To create an **superuser account**, use this command:

  $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

Getting Up and Running Locally With Docker
==========================================

The steps below will get you up and running with a local development environment.
All of these commands assume you are in the root of your project.

Prerequisites
-------------

* Docker
* Docker Compose

Build the Stack
---------------

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build

Reset and load data to the database
-----------------------------------

    $ docker system prune --volumes
    $ docker-compose -f local.yml up

# Create Admin user

   $ docker-compose -f local.yml run --rm django python manage.py create_elab_user

> Now you have an admin user :  email=admin@admin.com with  password="password"

Run the Stack
-------------

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py test
    $ docker-compose -f local.yml run --rm django pytest
    $ docker-compose -f local.yml run --rm django python manage.py shell_plus --notebook

# Add new ElabUser (TEACHER)

    $ docker-compose -f local.yml run --rm django python manage.py add_new_teacher  --email="user@example.com" --username="f_name l_name"

> after this command Elab user will recive an email containe
>
> * email : his email
> * password : length of 16

# Load Boards from Json file `Board.json`

$ docker-compose -f local.yml run --rm django python manage.py load_data

Execute Management Commands
---------------------------

As with any shell command that we wish to run in our container, this is done using the ``docker-compose -f local.yml run --rm`` command: ::

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py shell_plus
Here,``django`` is the target service we are executing the commands against.

Backups
-------

    $ docker-compose -f local.yml exec postgres backup
    $ docker cp 50b27d25021e:/db.json ./app/db.json
    $ docker- ps
    $ docker cp 5e9b64676deb:/backups ./backups
    $ docker-compose -f local.yml exec postgres restore backup_2020_06_02T08_18_57.sql.gz

Removing All Unused Objects
---------------------------

    $ docker stop $(docker ps -a -q)
    $ docker rm $(docker ps -a -q)
    $ docker system prune
    $ docker system prune --volumes

Generate diagram class with models
----------------------------------

    $ docker-compose -f local.yml run --rm django python manage.py graph_models -a -g -o models.png

Install CUBEProgrammer from drive [link]([https://drive.google.com/file/d/160__xzdtgtk8O4Pzpth3ytF7V-qpNjV9/view?usp=sharing]()) .. Copy paste it in `/STM32CubeProgrammer` folder .
--------------------------------------------------------------------

### Type checks

Running type checks with mypy:

    $ mypy pfa_backend

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd pfa_backend
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

## Deployment

The following details how to deploy this application.
