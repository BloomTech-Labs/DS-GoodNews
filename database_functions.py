from database import Database, db_session
from models import Story, Vote
import json

def dbAddVote(story_id, request):
    data = request.json
    print (data)
    story = Story.query.get(story_id)
    v = Vote()
    v.clickbait = data["clickbait"]
    v.voter_id = data["user_id"] 
    story.votes.append(v)
    db_session.add(story)
    db_session.commit()
    
def dbGet(story_id):
    story = Story.query.get(story_id)

    article_dictionary = story.to_dict()

    return json.dumps(article_information)

def dbGetByTimestamp(timestamp):
    result = Story.query.filter(Story.timestamp > timestamp )
    stories = []
    for story in result:
        article_dictionary = story.to_dict()
        stories.append(article_dictionary)

    return json.dumps(stories)