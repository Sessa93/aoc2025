#!/bin/bash
set -e

cd /aoc

RUNTIME_TYPE=${RUNTIME_TYPE:-execute}

if [ $RUNTIME_TYPE == "test" ]; then
  echo "Running tests..."
  exec pytest
elif [ $RUNTIME_TYPE == "execute-all" ]; then
  exec python ./src/main.py run-all
elif [ $RUNTIME_TYPE == "execute-single" ]; then
  DAY=exec python ./src/main.py run-single --day ${DAY} --problem ${PROBLEM}
else
  echo "Executing command"
  exec "$@"
fi