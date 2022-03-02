#!/bin/bash

rm -rf ./dataset/ml-latest-small
mkdir -p ./dataset
wget -O dataset-small.zip "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip" --no-check-certificate
unzip -j dataset-small.zip -d ./dataset/ml-latest-small


rm -f ./dataset/ml-latest-small/links.csv
rm -f ./dataset/ml-latest-small/tags.csv
rm -f ./dataset/ml-latest-small/README.txt
rm -f dataset-small.zip