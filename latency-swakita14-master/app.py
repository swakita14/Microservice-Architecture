from flask import Flask
import time
import os

app = Flask(__name__)




@app.route("/")
def hello():
	time.sleep(5)
	return "Hello World!"
 
if __name__ == "__main__":
    app.run()