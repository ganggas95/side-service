#!/bin/sh

export PYTHONUNBUFFERED=1
export ENV=local
export FLASK_APP=app
export FLASK_DEBUG=1
export DATABASE_URI=postgresql+psycopg2://root:b1sm1llah@side_users_db/side_db
export BACKEND_BASE_URL=api

# until test -z "$(ps -A | grep mysqld)"; do
#     >&2 echo "MySQL is unavailable - sleeping"
#     sleep 1
# done

# >&2 echo "MySQL is up - executing command"

# flask db init
# flask db migrate
# flask db upgrade

# python manage.py create_default_user

python manage.py runserver

# gunicorn --bind 0.0.0.0:$PORT app:instance \    
#     --workers 2 \
#     --timeout 300 \
#     --max-requests=2000 \
#     --keep-alive=2 \
#     --log-file=-