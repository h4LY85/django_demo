#!/usr/bin/env bash
# exit on error
set -o errexit

echo "hello start"

poetry env remove --all

poetry update
poetry install --no-dev --no-interaction

python manage.py collectstatic --no-input
python manage.py migrate
