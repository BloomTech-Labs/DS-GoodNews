from flask import Flask, request
from database import db_session
import stories as st

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(Exception=None):
    db_session.remove()

@app.route('/')
def goodnews():
    return 'Good News!'

@app.route('/stories/')
def stories():
    return st.update()

@app.route('/stories_2/')
def stories_2():
    return st.readall()

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host = '0.0.0.0', port = port)
    app.run()