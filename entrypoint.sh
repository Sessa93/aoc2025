#!/bin/bash
set -ex

cd /aoc

RUNTIME_TYPE=${RUNTIME_TYPE:-execute}

if [ $RUNTIME_TYPE == "test" ]; then
  echo "Running tests..."
  exec pytest
elif [ $RUNTIME_TYPE == "execute" ]; then
  exec python ./src/main.py
else
  echo "Executing command"
  exec "$@"
fi