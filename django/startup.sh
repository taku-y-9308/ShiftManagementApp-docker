#!/bin/sh

python manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi --bind=unix:/var/run/gunicorn/gunicorn.sock