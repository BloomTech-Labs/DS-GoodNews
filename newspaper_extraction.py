import datetime
import nltk
from newspaper import Article


def newspaperize(article_url):
    """Takes an article url and an id number. Returns a dictionary containing information scraped
    from the article"""

    article = Article(article_url)

    print("Downloading:", article_url)

    try:
        article.download()
    except:
        print("Failed to download url:", article_url)
        return None, None

    try:
        article.parse()
    except:
        print("Failed to parse url:", article_url)
        return None, None

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


