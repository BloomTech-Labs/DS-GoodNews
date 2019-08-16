import pandas as pd
import numpy as np

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.linear_model import LogisticRegression as LR
from sklearn.ensemble import RandomForestClassifier as RFC
import keras

from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score
from scipy.sparse import hstack
from keras.models import load_model

import nltk
from nltk import word_tokenize
nltk.download('all')


data = pd.read_csv('data/data.csv')
data.text = data.text.astype(str)

def getPosTags(text):
    posTags = nltk.pos_tag(nltk.word_tokenize(text))
    justTags = []
    for tags in posTags:
        justTags.append(tags[1])
    return justTags

data['posTags_list'] = data['text'].apply(lambda x: getPosTags(x))
data['posTags_string'] = data['posTags_list'].apply(lambda x: ' '.join([str(tag) for tag in x]))

tfidf_vectorizer_text = TfidfVectorizer()
tfidf_vectorizer_pos = TfidfVectorizer()

data_tfidf_text = tfidf_vectorizer_text.fit_transform(data['text'])
data_tfidf_pos = tfidf_vectorizer_pos.fit_transform(data['posTags_string'])

data_tfidf = hstack([data_tfidf_pos, data_tfidf_text]).toarray()
data_tfidf = pd.DataFrame(data_tfidf)

split = int(len(data)*0.75)
y_train = data['isClickbait'][:split].values
y_test = data['isClickbait'][split:].values
X_train = data_tfidf[:split].values
X_test = data_tfidf[split:].values

with open('pickles/svm.pkl', 'rb') as f:
    svm = joblib.load(f)
with open('pickles/mnb.pkl', 'rb') as f:
    mnb = joblib.load(f)
with open('pickles/lr.pkl', 'rb') as f:
    lr = joblib.load(f)
with open('pickles/rf.pkl', 'rb') as f:
    rf = joblib.load(f)
with open('pickles/neural_net.h5', 'rb') as f:
    nn = load_model('neural_net.h5')
with open('pickles/tfidf_vectorizer_pos.pkl', 'rb') as f:
    tfidf_vectorizer_pos = joblib.load(f)
with open('pickles/tfidf_vectorizer_text.pkl', 'rb') as f:
    tfidf_vectorizer_text = joblib.load(f)

models = {'Linear Support Vector': svm,
          'Multinomial Naive Bayes': mnb,
          'Logistic Regression': lr,
          'Random Forest': rf}
svm_predictions = svm.predict(X_test)
mnb_predictions = mnb.predict(X_test)
lr_predictions = lr.predict(X_test)
rf_predictions = rf.predict(X_test)
nn_predictions = nn.predict(X_test)
nn_predictions = [0 if i < 0.5 else 1 for i in nn_predictions]

all_predictions = zip(svm_predictions,
                      mnb_predictions,
                      lr_predictions,
                      rf_predictions,
                      nn_predictions)
final_predictions = []
for tup in all_predictions:
    final_predictions.append(max(set(list(tup)), key=list(tup).count))
print('ensemble', accuracy_score(y_test, final_predictions))
print('svm', accuracy_score(y_test, svm_predictions))
print('mb', accuracy_score(y_test, mnb_predictions))
print('lr', accuracy_score(y_test, lr_predictions))
print('rf', accuracy_score(y_test, rf_predictions))
print('nn', accuracy_score(y_test, nn_predictions))