# 8210projectT5
Heroku link

For Local Environment, please install requierements.txt:

Requirements: 
Django Version 2.1.7
Python Vesion 3.7
Virtual Environment Version 16.0.0

Getting Started:
1. Please install Python from https://www.python.org/downloads/
2. Create a Virtual Environment on your local machine by running "python3 -m venv env"
3. Run git init
4. git pull "https://github.com/ISQA-Classes/8210projectT5.git"
5. add local settings
6. Run "python manage.py migrate"
7. Run "python manage.py createsuperuser"


Local Settings Example:

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True


