#! /bin/bash
docker --version
docker login -u ${docker_credentials_USR} -p ${docker_credentials_PSW}
docker-compose build --parallel
docker-compose push 