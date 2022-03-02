# git repo
git clone

$HADOOP_HOME/sbin/start-dfs.sh


$HADOOP_HOME/sbin/start-yarn.sh

hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hdoop
hdfs dfs -put ./test-movies.csv /user/hdoop



hadoop jar ./hadoop-streaming-3.3.0.jar \
    -Dmapred.reuce.tasks=1 \
    -input /user/hdoop/test-movies.csv \
    -output /user/hdoop/output1 \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -file ~/test/coherent-training-konstantin-zboychik/Task5/mapper.py ~/test/coherent-training-konstantin-zboychik/Task5/reducer.py