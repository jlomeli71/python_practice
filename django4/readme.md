This foleder contains notes about django 4

# Instllation of django on pythonanywhere
https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial/

# Installation
mkvirtualenv django4 --python=/usr/bin/python3.10
pip install django

# when using the django virtual envirnment in pthonanywhere, use
workon django4

# verify dganjo is installed and version
python -m django --version

# clonning drchuck
git clone https://github.com/csev/dj4e-samples
# installing requirements
pip install -r requirements4.txt

# on the folder repository
python manage.py check
python manage.py makemigrations
python manage.py migrate

# back to home folder

mkdir django_projects
cd dganjo_projects
django-admin startproject mysite






----------------------------------------
# Running tutorial from django
django-admin startproject mysite

# This will create a mysite directory in your current director

tree mysite

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

cd mysite

# Before reloading and running the server
~/django_projects/mysite $ python3 manage.py check
reload

