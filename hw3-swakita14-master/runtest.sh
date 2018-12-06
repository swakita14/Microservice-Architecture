#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
export DB=activity-logger-app
export DB_USER=test_user
export DB_PASSWORD=swakita14
export DB_HOST=ds155073.mlab.com:55073

flask run --host=0.0.0.0 --port=5001