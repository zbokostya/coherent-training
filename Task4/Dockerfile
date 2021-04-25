FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive


#mysql
RUN apt-get update && \
  apt-get upgrade && \
  apt-get install -y git && \
  apt-get -yq install mysql-server && \
  rm -rf /var/lib/apt/lists/* && \
  mkdir -p /var/run/mysqld && \
  chown mysql:mysql /var/run/mysqld


# python
RUN apt-get update && \
  apt-get -y install python3-pip && \
  pip3 install mysql-connector-python

#git
RUN apt-get install git -y


# datasets
RUN apt-get install wget -y
RUN apt-get install unzip -y
RUN mkdir -p ~/dataset/{ml-latest-small,ml-latest-medium}
RUN wget -O ~/dataset-small.zip "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip" --no-check-certificate
RUN unzip -j ~/dataset-small.zip -d ~/dataset/ml-latest-small && \
  rm -f ~/dataset/ml-latest-small/links.csv && \
  rm -f ~/dataset/ml-latest-small/tags.csv && \
  rm -f ~/dataset/ml-latest-small/README.txt && \
  rm -f dataset-small.zip

ADD init.sh /init.sh
RUN chmod 755 /*.sh
ENTRYPOINT ["/init.sh"]

EXPOSE 3306
CMD ["mysqld_safe"]