import joblib
from keras.models import load_model
from scipy.sparse import hstack
import pandas as pd
import nltk
import os

global svm, mnb, lr, rf, nn, tfidf_vectorizer_text, tfidf_vectorizer_pos
dir_path = os.path.dirname(os.path.realpath(__file__))

pickle_file = os.path.join(dir_path, 'pickles')
svm_pickle_path = os.path.join(pickle_file, 'svm.pkl')
mnb_pickle_path = os.path.join(pickle_file, 'mnb.pkl')
lr_pickle_path = os.path.join(pickle_file, 'lr.pkl')
rf_pickle_path = os.path.join(pickle_file, 'rf.pkl')
nn_pickle_path = os.path.join(pickle_file, 'neural_net.h5')
pos_pickle_path = os.path.join(pickle_file, 'tfidf_vectorizer_pos.pkl')
text_pickle_path = os.path.join(pickle_file, 'tfidf_vectorizer_text.pkl')

with open(svm_pickle_path, 'rb') as f:
    svm = joblib.load(f)
with open(mnb_pickle_path, 'rb') as f:
    mnb = joblib.load(f)
with open(lr_pickle_path, 'rb') as f:
    lr = joblib.load(f)
with open(rf_pickle_path, 'rb') as f:
    rf = joblib.load(f)
nn = load_model(nn_pickle_path)

with open(pos_pickle_path, 'rb') as f:
    tfidf_vectorizer_pos = joblib.load(f)
with open(text_pickle_path, 'rb') as f:
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