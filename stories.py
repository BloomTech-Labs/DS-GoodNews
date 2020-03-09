import feedparser
import json
import random

from database import db_session
from database_functions import dbAddVote, dbGet, dbGetByTimestamp
from models import Story, Keyword, Vote, Feed
from newspaper_extraction import newspaperize
from classifier import classify_clickbait
import classifier

def update_feeds(list_of_RSS_feeds, all=False, sample=5):
    """Takes a list RSS feeds. Returns an updated list of recent article urls.
    Keyword arguments:
    all -- bool: True returns all urls
    sample -- int: amount of article urls to return  
    """ 
    list_of_article_urls = []
    for RSS_feed in list_of_RSS_feeds:
        feed = feedparser.parse(RSS_feed)
        for item in feed["items"]:
            list_of_article_urls.append(item['id'])

    return random.sample(population=list_of_article_urls, k=sample) if all is False else list_of_article_urls

def update_files(all=False, sample=5):

    feeds = Feed.query.all()
    list_of_RSS_feeds = [feed.url for feed in feeds]

    updated_article_urls = update_feeds(list_of_RSS_feeds, all, sample)

    new_article_jsons = []
    new_articles = []

    for url in updated_article_urls:
        s = Story.query.filter(Story.url == url).first()
        # NOTE: web app client need to handle if the article is updated
        print('URL Not Found in DB' if s is None else "URL Found in DB")
        if s is None:
            
            story = newspaperize(url)
            
            if story is not None:
                new_articles.append(story)

    for story_item in new_articles:
        story_item.clickbait = classify_clickbait(story_item.name)
        
    for story_item in new_articles:    
        if story_item is not None:
            db_session.add(story_item)
            db_session.commit()
            new_article_jsons.append(story_item.to_dict())
    
    return json.dumps(new_article_jsons) if all is False else ""



# database_functions
def AddVote(story_id, request):
    """Adds user's clickbait vote to story_id."""
    return dbAddVote(story_id, request)

def Get(story_id):
    """Get story information based on story_id"""
    return dbGet(story_id)

def GetByTimestamp(timestamp):
    """Get json of story information for every story after timestamp"""
    return dbGetByTimestamp(timestamp)



# update articles
def update_all():
    return update_files(all=True)

def update_sample(sample=5):
    return update_files(sample=sample)


