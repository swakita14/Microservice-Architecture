from flask import Flask, jsonify
import requests

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"


votes = [
    {
        'post_id': 0,
        'vote_count': -1,
    },
    {
        'post_id': 1,
        'vote_count': 5,
    },
    {
        'post_id': 2,
        'vote_count': 42,
    },
]
 


@app.route("/api/vote_count/<int:id>")
def get_single_votes(id):
    if id < 0 or id >= len(votes):
        abort(404)   
    return jsonify({"post_id": votes[id]['post_id']}, {"vote_count": votes[id]['vote_count']})


@app.route("/api/vote_count/")
def get_plural_votes():
    return jsonify(votes)

    