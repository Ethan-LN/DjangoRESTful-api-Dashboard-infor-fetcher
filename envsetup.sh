##set up enviroment for python 
#!/bin/bash

if [ -d "env" ]; then
    echo "Python virtual env exists"
else
    sudo python3.10 -m venv env
fi

echo $PWD
source env/bin/activate

sudo pip install -r requirements.txt

if [ -d "logs" ]; then
    echo "Log folder exists"
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
echo "envsetup finishes"






