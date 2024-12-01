#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations  # Adicione este comando para aplicar as migrações
python manage.py migrate  # Adicione este comando para aplicar as migrações