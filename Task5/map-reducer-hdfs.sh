#!/bin/bash

hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/zbokostya

hdfs dfs -rm -r /user/zbokostya/output

./download.sh

hdfs dfs -put ./dataset/ml-latest-medium/movies.csv  /user/zbokostya/input

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-input /user/zbokostya/movies.csv -output /user/zbokostya/output \
-file ./mapper.py ./reducer.py \
-mapper "python3 mapper.py" -reducer "python3 reducer.py"