import feedparser

def update_feeds(list_of_RSS_feeds):
    """ takes a list RSS feeds, a list containing article urls from the feeds, and a list containing
    the last update times of each feed. Returns an updated list of article urls and an updated list
    of last update times""" 
    list_of_article_urls = []
    for RSS_feed in list_of_RSS_feeds:
        feed = feedparser.parse(RSS_feed)
        for item in feed["items"]:
            list_of_article_urls.append(item['id'])

    return list_of_article_urls



from newspaper import Article
import nltk
import hashlib
nltk.download('punkt')

def newspaperize(article_url):
    """Takes an article url and an id number. Returns a dictionary containing information scraped
    from the article"""

    article = Article(article_url)

    try:
        article.download()
    except ArticleException:
        print("Failed to download url:", article_url)
        return None

    try:
        article.parse()
    except:
        print("Failed to download url:", article_url)
        return None

    headline = article.title
    timestamp = article.publish_date
    content = article.text
    article.nlp()
    keywords = article.keywords
    summary = article.summary
    description = article.meta_description
    id_number = hashlib.sha1(article_url.encode('utf-8')).hexdigest()
    
    # timestamp can be None
   
    article_information = {"id" : id_number,
                  "name": headline,
                  "url" : article_url,
                  "timestamp" : timestamp.isoformat() if timestamp is not None else "",
                  "description" : description,
                  "keywords" : keywords,
                  "summary" : summary,
                  "content" : content,
                  "clickbait" : None}
    
    return article_information



import jsonlines

def newspaperize_new_articles_from_feed(new_article_urls):
    new_article_jsons = []
    for article_url in new_article_urls:
        article_json = newspaperize(article_url)
        if article_json:
            new_article_jsons.append(article_json)
    return new_article_jsons

def update_files():
    
    with open('extracted_article_urls.txt') as f:
        extracted_article_urls = f.readlines()

    updated_article_urls = update_feeds(list_of_RSS_feeds)

    new_article_urls = list(set(updated_article_urls).difference(extracted_article_urls))

    new_article_jsons = newspaperize_new_articles_from_feed(new_article_urls)
   
    with open('extracted_article_urls.txt', 'a') as f:
        for url in new_article_urls:
            f.write(url + '\n')
    
    with jsonlines.open('data/articles.jsonl', mode = 'a') as f:
        for article_json in new_article_jsons: 
            f.write(article_json)
