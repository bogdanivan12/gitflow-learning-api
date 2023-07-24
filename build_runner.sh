#!/bin/bash

start_service () {
  docker stop "$1" && docker rm "$1"

  docker rmi "$1"

  docker build -f gitflow_learning_api/"$1"/Dockerfile_"$1" -t "$1" .

  if [ "$1" = "linkedlist" ]
  then
    service_port=8080
  else
    service_port=8081
  fi

  docker run -p "$service_port":"$service_port" --name "$1" "$1" &
}

set -x

SCRIPT_PATH=$(dirname "$0")

python3 -m pylint gitflow_learning_api \
  --init-hook="import sys; sys.path.append('$SCRIPT_PATH')" \
  --rcfile=.pylintrc

python3 -m pytest --disable-warnings

start_service linkedlist
start_service stringproc


#docker stop linkedlist && docker rm linkedlist
#
#docker rmi linkedlist
#
#docker build -f gitflow_learning_api/linkedlist/Dockerfile_linkedlist -t linkedlist .
#
#docker run -p 8080:8080 --name linkedlist linkedlist &


#docker stop stringproc && docker rm stringproc
#
#docker rmi stringproc
#
#docker build -f gitflow_learning_api/stringproc/Dockerfile_stringproc -t stringproc .
#
#docker run -p 8081:8081 --name stringproc stringproc &