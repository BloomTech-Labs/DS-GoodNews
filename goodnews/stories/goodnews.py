from flask import Flask
from flask import request
import stories as st
import database as db


app = Flask(__name__)

@app.route('/')
def goodnews():
    return 'Good News!'

@app.route('/stories/')
def stories():
    db.connect()
    return st.update()