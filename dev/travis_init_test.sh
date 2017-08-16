#!/usr/bin/env bash
# This initializes testing suite.
# Checks pep8 style of all python files
# also runs all unittests

#service mysql start

#spawn cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
#expect "password:"
#send "root"
#interact
#    && HBNB_MYSQL_USER=hbnb_dev \
#		      HBNB_MYSQL_PWD=hbnb_dev_pwd \
#		      HBNB_MYSQL_HOST=localhost \
#		      HBNB_MYSQL_DB=hbnb_dev_db \
#		      HBNB_TYPE_STORAGE=db \
#		      python3 -m unittest discover -v ./tests/ \

pep8 . && python3 -m unittest discover -v ./tests/

# stores the return value
ret_val=$?

# clears file.json
> ./dev/file.json

# removes __pycache__ folder
py3clean .

# exits with status from tests
exit "$ret_val"
