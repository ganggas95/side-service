#!/bin/sh

flask db init
flask db migrate
flask db upgrade

python manage.py create_default_user