import datetime
import nltk
from newspaper import Article
from stopwords import stopword
from models import Keyword, Story


def newspaperize(article_url):
    """Takes a string url that contains an article. Returns a Story object from 
    models.py containing information scraped from the article located at the url."""

    article = Article(article_url)

    print("Downloading:", article_url)

    try:
        article.download()
    except:
        print("Failed to download url:", article_url)
        return None

    try:
        article.parse()
    except:
        print("Failed to parse url:", article_url)
        return None

    headline = article.title
    imageurl = article.top_image
    timestamp = article.publish_date
    content = article.text
    article.nlp()
    keywords = article.keywords
    summary = article.summary
    description = article.meta_description
    clickbait = -1

    list_of_keyword_obj = []
    for word in keywords:
        if word not in stopword:
            k = Keyword()
            k.keyword = word
            list_of_keyword_obj.append(k)

    s = Story()
    s.name = headline
    s.imageurl = imageurl
    s.url = article_url
    current_time = datetime.datetime.now()
    if timestamp is not None:
        s.timestamp = timestamp.isoformat()
    else: # generate timestamp if none found
        s.timestamp = current_time
    # s.timestamp = timestamp.isoformat() if timestamp is not None else 
    s.description = description
    s.keywords = list_of_keyword_obj
    s.summary = summary
    s.content = content
    s.clickbait = clickbait
    s.createtime = current_time

    return s


