#!/bin/bash

export PYTHONPATH=$PYTHONPATH:$(pwd)

pipenv run alembic upgrade head

pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
