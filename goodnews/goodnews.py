from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def goodnews():
    return 'Good News!'

@app.route('/stories/')
def stories():
    with open('stories.json') as f:
        read_data = f.read()
    return read_data
