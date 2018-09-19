from flask import Flask
from flask import request
import stories as st

app = Flask(__name__)

@app.route('/')
def goodnews():
    return 'Good News!'

@app.route('/stories/')
def stories():
    return st.update()