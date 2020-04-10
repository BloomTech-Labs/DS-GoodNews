from flask import Flask, request, render_template
from flask_cors import CORS

import stories as st
from rq import Queue
from worker import conn

import datetime

q = Queue(connection=conn)
q.enqueue(st.update_all)

app = Flask(__name__)
CORS(app)

def schedule_update():
    """Calls update_all every five minutes"""
    q.enqueue(st.update_all)

@app.route('/update')
def update():
    return st.update_all()

@app.route('/')
def goodnews():
    """Landing page"""

    now = datetime.datetime.utcnow()
    query_time =  now - datetime.timedelta(days=1)
    timestamp = query_time.strftime('%Y-%m-%dT%H:%M:%S')
    # pass in False to return list of dict
    stories = st.GetByTimestamp(timestamp, False)
    sorted(stories, key = lambda i : i['timestamp'], reverse=True)
    return render_template('index.html', context = stories)

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
