from flask import Flask, jsonify

app = Flask(__name__)



def get_string_length(s):
	return len(s)

#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
def reverse_string(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse_string(s[1:]) + s[0] 

#https://thehelloworldprogram.com/python/python-string-methods/
def make_string_uppercase(s):
	return s.upper()





@app.route('/api/stringdata/<string:id>')
def get_string_attributes(id):

	return jsonify({"length":get_string_length(id), "reverse":reverse_string(id), "uppercase":make_string_uppercase(id)})