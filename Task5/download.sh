#!/bin/bash

rm -rf ./dataset/ml-latest-medium
mkdir -p ./dataset
wget -O dataset-medium.zip "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip" --no-check-certificate
unzip -j dataset-medium.zip -d ./dataset/ml-latest-medium


rm -f ./dataset/ml-latest-medium/ratings.csv
rm -f ./dataset/ml-latest-medium/links.csv
rm -f ./dataset/ml-latest-medium/tags.csv
rm -f ./dataset/ml-latest-medium/README.txt