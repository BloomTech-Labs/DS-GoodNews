from flask import Flask, request
from flask_cors import CORS

import stories as st

from rq import Queue
from worker import conn

q = Queue(connection=conn)

def schedule_update():
    q.enqueue(st.update_all)


app = Flask(__name__)
CORS(app)

@app.route('/')
def goodnews():
    return 'Good News!'

@app.route('/stories/')
def stories():
    timestamp = request.args.get('timestamp')
    if timestamp is not None:
        return st.GetByTimestamp(timestamp)
    else:
        return st.update()

@app.route('/stories/<int:story_id>', methods = ['POST', 'GET'])
def add_vote(story_id):
    if request.method == 'POST':
        st.AddVote(story_id, request)
        return ''
    if request.method == 'GET':
        return st.Get(story_id)


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host = '0.0.0.0', port = port)
    app.run()
