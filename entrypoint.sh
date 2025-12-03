#!/bin/bash
set -e

cd /aoc

RUNTIME_TYPE=${RUNTIME_TYPE:-execute}

if [ $RUNTIME_TYPE == "test" ]; then
  echo "Running tests..."
  exec pytest
elif [ $RUNTIME_TYPE == "execute-all" ]; then
  exec python ./src/main.py
elif [ $RUNTIME_TYPE == "execute-single" ]; then
  DAY=${DAY} PROBLEM=${PROBLEM} exec python ./src/main.py
else
  echo "Executing command"
  exec "$@"
fi