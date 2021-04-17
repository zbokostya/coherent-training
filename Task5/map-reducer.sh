#!/bin/bash

tail -n +2 ./dataset/ml-latest-medium/movies.csv | python3 mapper.py "$@" | sort | python3 reducer.py
#tail -n +2 test.txt | python3 mapper.py "$@" | python3 reducer.py