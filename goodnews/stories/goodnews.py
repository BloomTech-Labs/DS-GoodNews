from flask import Flask, request

import stories as st

app = Flask(__name__)

@app.route('/')
def goodnews():
    return 'Good News!'

@app.route('/stories/')
def stories():
    return st.update()

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host = '0.0.0.0', port = port)
    app.run()