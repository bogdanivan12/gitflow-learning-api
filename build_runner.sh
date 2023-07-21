#!/bin/bash

set -x

SCRIPT_PATH=$(dirname "$0")

python3 -m pylint gitflow_learning_api \
  --init-hook="import sys; sys.path.append('$SCRIPT_PATH')" \
  --rcfile=.pylintrc

python3 -m pytest --disable-warnings


docker stop linkedlist && docker rm linkedlist

docker rmi linkedlist

docker build -f gitflow_learning_api/linkedlist/Dockerfile_linkedlist -t linkedlist .

docker run -p 8080:8080 --name linkedlist linkedlist &


docker stop stringproc && docker rm stringproc

docker rmi stringproc

docker build -f gitflow_learning_api/stringproc/Dockerfile_stringproc -t stringproc .

docker run -p 8081:8081 --name stringproc stringproc &