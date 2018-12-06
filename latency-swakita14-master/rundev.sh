#!/bin/bash

export FLASK_APP=app.py
export HOST=localhost
export TIME=5

flask run --host=0.0.0.0 --port=5000