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
