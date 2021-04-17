#!/bin/bash

for arg do
  shift
  if [ "$arg" == "--getfiles" ]; then
    bash download.sh
    continue
  fi
  set -- "$@" "$arg"
done


bash map-reducer.sh "$@"