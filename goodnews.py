from flask import Flask, request, g

import stories as st

app = Flask(__name__)


with app.app_context():
    with open('svm.pkl', 'rb') as f:
        g.svm = joblib.load(f)
    with open('mnb.pkl', 'rb') as f:
        g.mnb = joblib.load(f)
    with open('lr.pkl', 'rb') as f:
        g.lr = joblib.load(f)
    with open('rf.pkl', 'rb') as f:
        g.rf = joblib.load(f)
    with open('neural_net.h5', 'rb') as f:
        g.nn = load_model('neural_net.h5')

    with open('tfidf_vectorizer_pos.pkl', 'rb') as f:
        g.tfidf_vectorizer_pos = joblib.load(f)
    with open('tfidf_vectorizer_text.pkl', 'rb') as f:
        g.tfidf_vectorizer_text = joblib.load(f)   
    print('models loaded')


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
    # svm, mnb, lr, rf, nn, tfidf_vectorizer_pos, tfidf_vectorizer_text = init()
    app.run()