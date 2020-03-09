import datetime # to get Story object creation time
# import nltk # necessary for NLP processing in newspaper
from newspaper import Article # Article object stores extracted information from urls
from stopwords import stopword # list of stopwords to remove from keywords
from models import Keyword, Story # Keyword and Story objects to store keywords and story information


def newspaperize(article_url):
    """Takes a string url that contains an article. Returns a Story object from 
    models.py containing information scraped from the article located at the url."""

    article = Article(article_url) # create Article object

    print("Downloading:", article_url)

    try: # returns None if url fails to download
        article.download()
    except:
        print("Failed to download url:", article_url)
        return None

    try: # returns None if url cannot be parsed
        article.parse()
    except:
        print("Failed to parse url:", article_url)
        return None

    article.nlp()

    # variables to hold values for Story attributes
    headline = article.title
    imageurl = article.top_image
    timestamp = article.publish_date
    content = article.text
    keywords = article.keywords
    summary = article.summary
    description = article.meta_description
    clickbait = -1 # placeholder for clickbait label

    # populates keyword object with article.keywords
    list_of_keyword_obj = []
    for word in keywords:
        if word not in stopword: # prevents stopwords from being keywords
            k = Keyword()
            k.keyword = word
            list_of_keyword_obj.append(k)


    s = Story() # create Story object

    # set attributes
    s.name = headline
    s.imageurl = imageurl
    s.url = article_url
    current_time = datetime.datetime.now()

    if timestamp is not None:
        s.timestamp = timestamp.isoformat()
    else: # generate timestamp if none found
        s.timestamp = current_time 

    s.description = description
    s.keywords = list_of_keyword_obj
    s.summary = summary
    s.content = content
    s.clickbait = clickbait
    s.createtime = current_time

    return s


