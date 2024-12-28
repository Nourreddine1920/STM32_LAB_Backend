# SM32 LAB Backend

Welcome to the **STM32 LAB Backend Project**, a robust STM32 LAB application developed using **Django**. This application powers the **eLAB platform**, enabling user management, data handling, and seamless deployment with **Docker**. It's designed with scalability, performance, and developer experience in mind.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)  
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

---

## 📄 **License**  
This project is licensed under the **MIT License**.

---

## 🔧 **Project Settings**  
For a detailed explanation of settings, refer to the [Cookiecutter Django Settings Documentation](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

---

## 🚀 **Getting Started**

### Prerequisites
Before setting up the project, ensure you have the following installed:
- **Docker**  
- **Docker Compose**

---

## 🛠️ **Setting Up the Project**

### Building the Docker Stack
To build the application stack for the first time, run:
```bash
docker-compose -f local.yml build
```

### Running the Project Locally
Bring up the development environment with:
```bash
docker-compose -f local.yml up
```

### Database Migration
After the stack is up, apply migrations:
```bash
docker-compose -f local.yml run --rm django python manage.py migrate
```

### Creating an Admin User
Set up a superuser account:
```bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

---

## 🔑 **User Management**

### Creating Users
#### Normal User
1. Visit the **Sign Up** page.
2. Complete the form and verify the email from the simulated console message.

#### Admin User
Create an admin user by running:
```bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

#### Add a New Teacher
To create a teacher account, use:
```bash
docker-compose -f local.yml run --rm django python manage.py add_new_teacher --email="user@example.com" --username="FirstName LastName"
```
The teacher will receive an email containing:
- **Email:** Provided email
- **Password:** Auto-generated (16 characters)

---

## 📊 **Data Management**

### Loading Data
Load `Board.json` to the database:
```bash
docker-compose -f local.yml run --rm django python manage.py load_data
```

### Resetting the Database
To prune volumes and reset the database:
```bash
docker system prune --volumes
docker-compose -f local.yml up
```

---

## 🔍 **Testing and Quality Checks**

### Running Tests
Run tests using:
```bash
docker-compose -f local.yml run --rm django python manage.py test
docker-compose -f local.yml run --rm django pytest
```

### Checking Test Coverage
```bash
coverage run -m pytest
coverage html
open htmlcov/index.html
```

### Type Checks
Run static type checks with:
```bash
mypy stm32_lab_backend
```

---

## 🎨 **Development Enhancements**

### Live Reloading and SASS Compilation
For live reloading and CSS changes, refer to the [Cookiecutter Django Docs](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Generating Class Diagrams
Generate diagrams for your Django models with:
```bash
docker-compose -f local.yml run --rm django python manage.py graph_models -a -g -o models.png
```

---

## ♻️ **Maintenance Commands**

### Backups
To back up the database:
```bash
docker-compose -f local.yml exec postgres backup
docker cp <container_id>:/db.json ./app/db.json
```

### Restoring Backups
To restore a previous backup:
```bash
docker-compose -f local.yml exec postgres restore backup_<timestamp>.sql.gz
```

### Cleaning Up Unused Objects
To remove unused containers, volumes, and images:
```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune --volumes
```

---

## 🔄 **Running Celery**

This application comes with **Celery** for asynchronous task processing.

### Running a Celery Worker
To start a worker:
```bash
cd stm32_lab_backend
celery -A config.celery_app worker -l info
```
Ensure you are in the same folder as `manage.py` when running Celery commands.

---

## 🚀 **Deployment**

For deployment instructions, refer to the [Cookiecutter Django Deployment Documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
