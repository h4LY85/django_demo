#!/usr/bin/env bash
# exit on error
set -o errexit
pip install --upgrade poetry
poetry env remove --all
poetry add "rembg@^2.0.64" "onnxruntime@^1.16.3"
poetry install --no-dev --no-interaction

python manage.py collectstatic --no-input
python manage.py migrate
