import json
import requests

response = requests.get('https://reqres.in/api/users/')
data = response.json()
first_name = data["data"][1]["first_name"]
last_name = data["data"][1]["last_name"]

print(first_name + " " + last_name)