from sklearn.externals import joblib
from keras.models import load_model
from scipy.sparse import hstack
import pandas as pd
import nltk

global svm, mnb, lr, rf, nn, tfidf_vectorizer_text, tfidf_vectorizer_pos

with open('pickles/svm.pkl', 'rb') as f:
    svm = joblib.load(f)
with open('pickles/mnb.pkl', 'rb') as f:
    mnb = joblib.load(f)
with open('pickles/lr.pkl', 'rb') as f:
    lr = joblib.load(f)
with open('pickles/rf.pkl', 'rb') as f:
    rf = joblib.load(f)
nn = load_model('pickles/neural_net.h5')

with open('pickles/tfidf_vectorizer_pos.pkl', 'rb') as f:
    tfidf_vectorizer_pos = joblib.load(f)
with open('pickles/tfidf_vectorizer_text.pkl', 'rb') as f:
    tfidf_vectorizer_text = joblib.load(f)

def classify_clickbait(headline):
    
    def getPosTags(text):
        posTags = nltk.pos_tag(nltk.word_tokenize(text))
        justTags = []
        for tags in posTags:
            justTags.append(tags[1])
        return justTags
    
    headline_pos = getPosTags(headline)
    headline_pos = ' '.join([str(tag) for tag in headline_pos])

    data_tfidf_text = tfidf_vectorizer_text.transform([headline])
    data_tfidf_pos = tfidf_vectorizer_pos.transform([headline_pos])

    data_tfidf = hstack([data_tfidf_pos, data_tfidf_text]).toarray()
    data_tfidf = pd.DataFrame(data_tfidf)

    nn_pred = nn.predict(data_tfidf)
    nn_pred = [0 if i < 0.5 else 1 for i in nn_pred][0]

    predictions = [int(svm.predict(data_tfidf)[0]),
                   int(mnb.predict(data_tfidf)[0]),
                   int(lr.predict(data_tfidf)[0]),
                   int(rf.predict(data_tfidf)[0]),
                   nn_pred]

    return max(set(predictions), key=predictions.count)