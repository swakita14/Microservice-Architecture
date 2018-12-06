from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from mongoengine import *
from pymongo import MongoClient
import json
import os
import time


app = Flask(__name__)


sleep_time = os.getenv('SLEEP_TIME', default=0)

mongo_host = os.getenv('DB_HOST')
mongo_db = os.getenv('DB')
mongo_user = os.getenv('DB_USER')
mongo_password = os.getenv('DB_PASSWORD')

connect(db=mongo_db,
        host=mongo_host,
        username=mongo_user,
        password=mongo_password)

class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow())
    #location = StringField(required=True, max_length=64)
    details = StringField(required=True)

def helper_json_to_user_view(request):
	json_data = {}
	json_data = request.get_json()
	json_data["location"] = url_for("activities", id=a.id)
	return json_data

@app.route("/api/activities/<string:id>", methods=["GET"])
def activities(id):
	a = ActivityLog.objects.get(id=id)
	return a.to_json()


@app.route("/api/activities/", methods=["GET"])
def activity():
	items = ActivityLog.objects.limit(10).order_by("-timestamp")
	return items.to_json()


@app.route("/api/activities", methods=["POST"])
def new_activities():
	if not request.json:
		abort(400, "Missing element")
	new_usr = request.get_json()
	if "user_id" not in new_usr or "username" not in new_usr or "details" not in new_usr:
		abort(400, "ID should be part of the request")
	insert = ActivityLog(
		user_id = new_usr["user_id"],
		username = new_usr["username"],
		details = new_usr["details"],
	)
	
	insert.save()
	time.sleep(int(sleep_time))
	new_usr["location"] = url_for("activities", id=insert.id)
	new_usr["id"] = str(insert.id)

	return jsonify(new_usr), 201


	
