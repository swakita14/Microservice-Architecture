from flask import Flask, jsonify

app = Flask(__name__)




def divisors(num):
    possibles = list(range(1, num+1))

    divisorList = []

    for number in possibles:
        if num % number == 0:
            divisorList.append(number)

    return divisorList



@app.route('/')
def hello_world():
    	return "Hello World!"

@app.route('/api/divisors/<int:id>')
def get_divisors(id):
    items = divisors(id)

    return jsonify({"divisors": items})