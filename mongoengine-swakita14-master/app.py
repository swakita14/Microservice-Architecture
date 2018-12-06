from mongoengine import *
import os
from datetime import datetime

mongo_host = os.getenv('DB_HOST')
mongo_db = os.getenv('DB')
mongo_user = os.getenv('DB_USER')
mongo_password = os.getenv('DB_PASSWORD')

connect(db=mongo_db,
        host=mongo_host,
        username=mongo_user,
        password=mongo_password)

class BusinessProject(Document):
    owner_id = IntField(required=True)
    project_name = StringField(required=True, max_length=64)
    due_date = DateTimeField(default=datetime.utcnow)
    project_details = StringField(required=True)


insert = BusinessProject(
		owner_id = 5,
		project_name = "in-class",
		due_date = datetime.utcnow,
		project_details= "this is going to be tough",
	)

insert.save()

print(insert.owner_id)