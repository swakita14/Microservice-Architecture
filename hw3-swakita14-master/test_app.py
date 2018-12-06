import pytest
from flask import url_for
import os
from app import app
from mongoengine import *

@pytest.fixture
def client():
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["SERVER_NAME"] = "test.local"
    mongo_host = os.environ.get('HOST')
    mongo_db = os.environ.get('DB')
    client = app.test_client()
    ids = os.environ.get('ID')
    db = connect(db=mongo_db, host=mongo_host)
    db.drop_database("activity_log_test")
    db.close()
    db = connect(db=mongo_db, host=mongo_host)

    # Pushing the app context allows us to make calls to the app like url_for
    # as if we were the running Flask app. Makes testing routes more resilient.
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()

def test_get_plural_list_of_individual_activities(client):
	response = client.get(url_for("activity"))
	assert response.status_code == 200
	#assert "/login" in response.headers["Location"]



def test_post_new_Activities_when_json_not_sent(client):
	response = client.post(url_for("new_activities"))
	assert response.status_code==400


