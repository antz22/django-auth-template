# Django DRF Authentication Template

Project template for django with the django-rest-framework and djoser to allow for easy building of restful APIs and authentication.

Packages:
- [django-rest-framework](https://www.django-rest-framework.org) for building APIs and serializers
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) for CORS security
- [djoser](https://github.com/sunscrapers/djoser) for handling of authentication

Features:
- Adds template code for models.py, serializers.py and urls.py
- Creates views.py functions and urls for APIView of the example model and creating an example model
- Adds django-cors-headers security and middleware in settings.py
- Registers example models in admin.py

## Installation

In your terminal, run these commands.

First, clone the repository to get the files on your local system.

```shell
$ git clone https://github.com/antz22/django-auth-template.git
$ cd django-auth-template
$ cd project_name
```

To rename the project, navigate to project_name/settings.py and change the following variables:
```python
ROOT_URLCONF = 'NEW_project_name.urls'
WSGI_APPLICATION = 'NEW_project_name.wsgi.application'
```

Then, go to project_name/wsgi.py and change this:
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEW_project_name.settings')
```

In the root directory, change this line in manage.py:
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEW_project_name.settings')
```

Lastly, rename the folders in your project.

At this point, if you would like, you can move the 'project_name' django project to a different folder, outside the github repo folder.

Then, create a virtual environment for your pip dependencies. Depending on your OS, this command might be different. To install virtualenv, do 'pip install virtualenv'.
(in project_name directory)

```shell
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```


Finally, initialize the database and create an admin user. For createsuperuser, you can leave the email field blank and call your username 'admin'.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

To run the server, use the following.

```shell
$ python manage.py runserver
```

You can navigate to the 127.0.0.1:8000/admin url and login with your superuser credentials to access the database.


Happy coding!