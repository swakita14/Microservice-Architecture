from flask import Flask, abort, render_template
import json
import requests


app = Flask(__name__)

posts = [
    {
        'id': 0,
        'title': "Interesting post",
        'content': 'Lorem ipsum etc.',
        'author': 'Poe',
    },
    {
        'id': 1,
        'title': "Storing data from csv file",
        'content': 'So I wanted a project that included a gui so I decided to write a script that would help me calculate wind adjustments (and maybe other stuff down the line) for playing Golf Clash. Basically every club has an "accuracy" and is affected differently depending on wind strength. I created a spreadsheet containing all the attributes for each club and saved it as a csv file. Here is a small sample...',  # noqa: E501
        'author': 'Joe',
    },
    {
        'id': 2,
        'title': "Django Rest Framework serialisation",
        'content': "I'm new to Python/Django and having trouble trying to serialize a N-N relation using Django Rest Framework.",  # noqa: E501
        'author': 'Moe',
    },
]




@app.route('/')
def index():
    response = requests.get('http://0.0.0.0:5001/api/vote_count/')
    data = response.json()
    post = posts[data[0]['post_id']]
    votes = data
    
    
    return render_template(
        "index.html",
        title="Microblog for Microservices",
        posts=posts,
        votes=votes,
    )


@app.route('/post/<int:post_id>')
def post(post_id):
    response = requests.get('http://0.0.0.0:5001/api/vote_count/'+ str(post_id))
    data = response.json()   
    if post_id < 0 or post_id >= len(posts):
        abort(404)
    post = posts[data[0]['post_id']]
    vote_count = data[1]['vote_count']
    return render_template(
        "post.html",
        title=post['title'],
        post=post,
        vote_count=vote_count,
    )
