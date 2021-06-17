#! bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Loading..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep .1
    done

    echo 'Postgres started!'
    echo 'hulahoo'

fi

python3 manage.py flush --no-input
python3 manage.py migrate

exec '$@'