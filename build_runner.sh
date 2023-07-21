#!/bin/bash

set -x

SCRIPT_PATH=$(dirname "$0")

python3 -m pylint gitflow_learning_api \
  --init-hook="import sys; sys.path.append('$SCRIPT_PATH')" \
  --rcfile=.pylintrc

python3 -m pytest --disable-warnings