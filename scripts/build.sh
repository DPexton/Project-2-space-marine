#! /bin/bash
docker --version
docker-compose down --rmi all
docker login -u ${docker_credentials_USR} -p ${docker_credentials_PSW}
docker-compose build
docker-compose push 