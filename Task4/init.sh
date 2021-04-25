#!/bin/bash

# mysql
TEMP_FILE='/tmp/mysql-first-time.sql'
cat > "$TEMP_FILE" <<-EOSQL
  CREATE USER 'zbokostya'@'%' IDENTIFIED BY 'zFh3gm0BLnwb' ;
  GRANT ALL ON *.* TO 'zbokostya'@'%' WITH GRANT OPTION ;
  FLUSH PRIVILEGES ;
EOSQL

# git
if [ -n "$GIT_PASSWORD" ] ; then
  git clone https://zbokostya:"$GIT_PASSWORD"@bitbucket.org/coherentprojects/coherent-training-konstantin-zboychik.git;
  set -- "$@" --init-file="$TEMP_FILE"
fi

exec "$@"
