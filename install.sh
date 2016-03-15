#! /bin/bash
# use this script only once to get the preparations

# run migrations, creates superuser and fill the DB
venv/bin/python board/manage.py migrate
venv/bin/python board/manage.py createsuperuser
