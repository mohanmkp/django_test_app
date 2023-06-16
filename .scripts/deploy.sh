#!/bin/bash

set -e
sudo pwd
cd /home/apps/django_test_app/
git pull
echo "changes pulling"

echo "venv activating"
source  venv/bin/activate
echo "venv activated"

echo "install requirements"
pip install -r requirements.txt
echo "requirements installed"


echo "setup app"
python manage.py makemigrations
python manage.py migrate


echo "start server"
#python manage.py runserver 0.0.0.0:8000


