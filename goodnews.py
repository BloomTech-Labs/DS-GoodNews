from flask import Flask, request
from flask_cors import CORS

import stories as st
from rq import Queue
from worker import conn

q = Queue(connection=conn)
q.enqueue(st.update_all)

app = Flask(__name__)
CORS(app)

def schedule_update():
    """Calls update_all every five minutes"""
    q.enqueue(st.update_all)

@app.route('/')
def goodnews():
    """Landing page"""
    return 'Good News!'

@app.route('/stories/')
def stories():
    """Return all stories after timestamp inputted"""
    timestamp = request.args.get('timestamp')
    if timestamp is not None:
        return st.GetByTimestamp(timestamp)
    else:
        return 'Input timestamp please'

@app.route('/stories/<int:story_id>', methods = ['POST', 'GET'])
def add_vote(story_id):
    """Adds users vote to story_id"""
    if request.method == 'POST':
        st.AddVote(story_id, request)
        return ''
    if request.method == 'GET':
        return st.Get(story_id)

if __name__ == '__main__':
    app.run()
