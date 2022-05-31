#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi --bind=unix:/var/run/gunicorn/gunicorn.sock