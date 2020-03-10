#!/usr/bin/env sh
gunicorn  -w 3 --bind :5000 wsgi:app
