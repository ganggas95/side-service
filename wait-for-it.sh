#!/bin/sh

export PYTHONUNBUFFERED=1
export ENV=local
export HOST=0.0.0.0
export PORT=9091
export FLASK_APP=app
export FLASK_DEBUG=1
export DATABASE_URI=mysql+pymysql://root:b1sm1llah@side_users_db/side_users_db
export BACKEND_BASE_URL=api

until test -z "$(ps -A | grep mysqld)"; do
    >&2 echo "MySQL is unavailable - sleeping"
    sleep 1
done

>&2 echo "MySQL is up - executing command"

flask db init
flask db migrate
flask db upgrade

# python manage.py create_default_user

python manage.py runserver