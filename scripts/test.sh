
#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip 
sudo apt-get install python3-venv y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install requests-mock


python3 -m pytest frontend --junitxml=junit/test_frontend.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest chapter --junitxml=junit/test_chapter.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest role --junitxml=junit/test_role.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest name --junitxml=junit/test_name.xml --cov=app --cov-report=xml --cov-report=html