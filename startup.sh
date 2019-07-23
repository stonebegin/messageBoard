#!/usr/bin/env bash
python manage.py collectstatic --noinput &&
python manage.py migrate &&
gunicorn django_web_app.wsgi:application -w 2 -b :8002