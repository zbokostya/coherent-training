#!/bin/bash


for arg do
  shift
  if [[ "$arg" == -N* ]]; then
    NCount="$arg"
    continue
  fi
  set -- "$@" "$arg"
done

tail -n +2 ./dataset/ml-latest-medium/movies.csv | python3 mapper.py "$@" | python3 reducer.py "$NCount"