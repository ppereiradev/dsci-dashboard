#!/bin/sh
set -e

ls -la /home/user/vol/
ls -la /home/user/vol/web

# to clean all informations from database just uncomment this line
#python manage.py flush --no-input

# waiting and checking if database container is up
python manage.py wait_for_db

# preparing models to create database
python manage.py makemigrations


# creating records to models
python manage.py migrate accounts --noinput
python manage.py migrate admin --noinput
python manage.py migrate auth --noinput
python manage.py migrate contenttypes --noinput
python manage.py migrate sessions --noinput

# django_plotly_dash has a problem when using pymongo, so we have to fake migrate
python manage.py migrate django_plotly_dash --fake --noinput

# adding superuser
python manage.py default_users --superuser=yes --username=$DJANGO_SUPERUSER_USERNAME \
    --email=$DJANGO_SUPERUSER_EMAIL \
    --password=$DJANGO_SUPERUSER_PASSWORD

# adding user diretoria
python manage.py default_users --username=$DJANGO_DIRETORIA_USERNAME \
    --email=$DJANGO_DIRETORIA_EMAIL \
    --password=$DJANGO_DIRETORIA_PASSWORD

# adding user corporativa
python manage.py default_users --username=$DJANGO_CORPORATIVAS_USERNAME \
    --email=$DJANGO_CORPORATIVAS_EMAIL \
    --password=$DJANGO_CORPORATIVAS_PASSWORD

# adding user conectividade
python manage.py default_users --username=$DJANGO_CONECTIVIDADE_USERNAME \
    --email=$DJANGO_CONECTIVIDADE_EMAIL \
    --password=$DJANGO_CONECTIVIDADE_PASSWORD


python manage.py collectstatic --noinput

gunicorn app.wsgi:application --bind 0.0.0.0:8000