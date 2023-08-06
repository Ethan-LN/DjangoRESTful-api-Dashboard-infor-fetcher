#!bin/bash

echo"$PWD"

. env/bin/activate

cd /var/lib/jenkins/workspace/django-cicd/app/

python3 manage.py makemigrations
pythin3 manage.py migrate

echo "migration has been done"

cd /var/lib/jenkins/workspace/django-cicd/

sudo cp -rf guniorn.socket /etc/systemd/system/

sudo cp -rf guniorn.service /etc/systemd/system/

echo "$USER"
echo= "$PWD"

sudo systemctl daemon-reload
sudo systemtl start gunicorn
sudo systemtl enable gunicorn

ehco "Gunicorn has been started"

sudo systemctl status gunicorn
sudo systemctl restart gunicorn