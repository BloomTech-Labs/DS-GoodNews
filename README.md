# DS-GoodNews
Data science and analysis for the Good News project

## Good News Project
The Good News Project is a news aggregator that uses machine learning to remove clickbait news articles. In a model where ad revenue is driven by clicks, some publisher's have chosen to maximize click rate instead of providing valuable news to the reader. With the Good News Project, users get informative and worthwhile news articles without limiting their range of news sources. 

## News Sources
The sources of the news articles

## Dataset
Two datasets were combined to analyze clickbait articles and train the classifiers:

The first dataset contained only headlines and a label. Headlines retrieved from ‘WikiNews’, ’New York Times’, ‘The Guardian’, and ‘The Hindu’ were automatically labeled as non-clickbait. Headlines labeled clickbait were retrieved from ‘BuzzFeed’, ‘Upworthy’, ‘ViralNova’, ‘Thatscoop’, ‘Scoopwhoop’ and ‘ViralStories’ and then subjected to a manual review process.

Abhijnan Chakraborty, Bhargavi Paranjape, Sourya Kakarla, and Niloy Ganguly. "Stop Clickbait: Detecting and Preventing Clickbaits in Online News Media”. In Proceedings of the 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM), San Fransisco, US, August 2016.

https://github.com/bhargaviparanjape/clickbait/tree/master/dataset

The second dataset was created for the Clickbait Challenge 2017 competition.  Headlines were presented to annotators who rated a social media post on how clickbaiting it was on a four point scale. At least five annotators labeled each post.  It is unclear whether the annotators viewed only the headline, or the article content as well.  The social media post often closely followed the headline.

https://www.clickbait-challenge.org/

### Future Dataset

The evaluate clickbait feature will enable users to label articles as clickbait or not. This direct input from the user is more useful than the datasets that were publicly available, and it will be used to continually retrain our models.

## Article JSON format:
```json
{
	"id" : "<id>",
	"name": "<headline>",
	"url" : "<url>",
	"timestamp" : "<date time of publication>",
	"description" : "<description>",
	"keywords" : "<keywords>",
	"summary" : "<summary>",
	"content" : "<content>",
	"clickbait" : "<binary_classification>"
}
```
Except id, all these fields can be extracted with the newspaper library given the url.

## Natural Language Processing

### Term Frequency Inverse Document Frequency
The most effective processing of the headline text was tf-idf.  Count frequency and bigram frequency were not only less accurate, but took more time and memory. TensorFlow Hub's Universal Sentence Encoder also did not perform as well in our models as tf-idf.


### Parts of Speech Tagger
In addition to using tf-idf to vectorize the text of the headline, the words in each headline were also converted into their parts of speech tags to create another 'headline' that only contained the ordered parts of speech tags. This again was vectorized with tf-idf and then appended to the original headline vectorization. This combination of text and parts of speech tags increased accuracy by roughly one percent.

## Classifiers
The classifiers used to determine whether an article is clickbait or not:

### Support Vector Machine
The support vector machine can be used in classification tasks. It is effective in high-dimensional spaces, as is the case here with vectorized text. Despite the high-dimensionality of the space, however, it is still memory efficient.

### Multinomial Naive Bayes 
The multinomial naive bayes model is a a variant of naive bayes that is effective at classifying vectorized text.

### Logistic Regression
Logistic regression was used because it is a generally robust model that can operate efficiently in a high-dimensional space.

### Neural Net
Although neural nets tell us little about important predictors in the data, or their relationship to other points in the dataset, neural nets can be highly accurate at classifying text.  Here, we used a simple neural net to quickly reach above 95% accuracy.

### Random Forest
The random forest classifier was chosen due to the possibility that the key placement of only a few words in the headline, such as 'you' or 'believe', were linked to whether an article was clickbait or not. The random forest classifier achieves a similar accuracy as the other models, but is costly in terms of memory and time. 



## Tech Stacks
All the codes are written in Python.
We use the Flask microframework as the backend to serve these articles/stories to client applications via RESTful web services.
We use SQLAlchemy on top of PostgreSQL for database.

Natural language processing of the articles was done using newspaper, which is built on NLTK (Natural Language Toolkit). The headlines were vectorized with sci-kit learn's tfidf vectorizer and parts of speech were extracted with NLTK.

## Web API
Method GET /stories/?timestamp={timestamp}
Get non-clickbait stories after the timestamp
	
Method GET /stories/{id}
Get a particular story based on the story id

Method POST /stories/{id}  BODY: {"user_id" : 1213, "clickbait" : true}
Use to report clickbait or non-clickbait 
