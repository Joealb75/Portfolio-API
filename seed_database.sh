#!/bin/bash

rm db.sqlite3
rm -rf ./portfolioapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations portfolioapi
python3 manage.py migrate portfolioapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

