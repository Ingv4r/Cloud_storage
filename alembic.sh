#!/bin/bash

# To start alembic, run:
alembic init <name of dir (migrations)>

# To create revisions (makemigrations, aka Django), run:
alembic revision --autogenerate -m "<NAME OF MIGRATION>"

# To run migrations
alembic upgrade 'name of revision in /verions/smth.py'