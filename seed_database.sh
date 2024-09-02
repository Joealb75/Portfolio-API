#!/bin/bash

# Remove database and migrations if they exist
if [ -f db.sqlite3 ]; then
    rm db.sqlite3
fi

if [ -d ./portfolioapi/migrations ]; then
    rm -rf ./portfolioapi/migrations
fi
python3 manage.py migrate
python3 manage.py makemigrations portfolioapi
python3 manage.py migrate portfolioapi
#python3 manage.py loaddata users
#python3 manage.py loaddata tokens
python3 manage.py loaddata tags.json
python3 manage.py loaddata projects.json
python3 manage.py loaddata images.json

