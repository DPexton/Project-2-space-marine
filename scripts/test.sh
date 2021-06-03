#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip

pip3 install -r requirements.txt
pip3 install requests-mock

export DATABASE_URI


python3 -m pytest front-end --junitxml=junit/test_results.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest operator_random --junitxml=junit/test_results1.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest strat_random --junitxml=junit/test_results2.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest points --junitxml=junit/test_results3.xml --cov=app --cov-report=xml --cov-report=html