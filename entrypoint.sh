#!/bin/bash
set -e

cd /app/database

if [ ! -f "alembic/versions/.init_done" ]; then
    alembic revision --autogenerate -m "Init"
    touch alembic/versions/.init_done
fi

alembic upgrade head

cd /app

exec "$@"
