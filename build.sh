#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
poetry export -f requirements.txt --output requirements.txt --without-hashes
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
