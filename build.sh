#!/usr/bin/env bash
# Build script run by Render on every deploy.
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
