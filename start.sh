#!/bin/sh
export FLASK_APP=./app/__init__.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 -p 8080
