#! /bin/bash
docker --version
docker-compose down --rmi all
docker login -u ${docker-credentials_USR} -p ${docker-credentials_PSW}
docker-compose build
docker-compose push 