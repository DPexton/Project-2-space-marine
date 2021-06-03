#! /bin/bash
cd frontend/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report=html --cov-report=xml

cd ..

cd chapter/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report=html --cov-report=xml

cd ..

cd role/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report=html --cov-report=xml

cd ..

cd name/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report=html --cov-report=xml