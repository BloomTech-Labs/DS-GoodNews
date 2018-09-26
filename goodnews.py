from flask import Flask, request

import stories as st

app = Flask(__name__)

global svm, mnb, lr, rf, nn, tfidf_vectorizer_pos, tfidf_vectorizer_text

def init():
    with open('svm.pkl', 'rb') as f:
        svm = joblib.load(f)
    with open('mnb.pkl', 'rb') as f:
        mnb = joblib.load(f)
    with open('lr.pkl', 'rb') as f:
        lr = joblib.load(f)
    with open('rf.pkl', 'rb') as f:
        rf = joblib.load(f)
    with open('neural_net.h5', 'rb') as f:
        nn = load_model('neural_net.h5')

    with open('tfidf_vectorizer_pos.pkl', 'rb') as f:
        tfidf_vectorizer_pos = joblib.load(f)
    with open('tfidf_vectorizer_text.pkl', 'rb') as f:
        tfidf_vectorizer_text = joblib.load(f)
    
    print('models loaded')
    return svm, mnb, lr, rf, nn, tfidf_vectorizer_pos, tfidf_vectorizer_text



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
    svm, mnb, lr, rf, nn, tfidf_vectorizer_pos, tfidf_vectorizer_text = init()
    app.run()