from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import mapper, relationship
from database import Base 

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.id'))
    clickbait = Column(Boolean)
    voter_id = Column(String)

    def __init__(self, voter_id = None):
        self.voter_id = voter_id

    def __repr__(self):
        return '<ClickBait>:%r' % (self.clickbait)


class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.id'))
    keyword = Column(String)

    def __init__(self, word=None):
        self.keyword = word

    def __repr__(self):
        return '%r' % (self.keyword)

class Story(Base):

    __tablename__ = "stories"

    id = Column(Integer, primary_key = True)
    name = Column(String(256))
    imageurl = Column(String(1024))
    url = Column(String(1024))
    timestamp = Column(DateTime)
    description = Column(String())
    keywords = relationship("Keyword")
    summary = Column(String())
    content = Column(String())
    clickbait = Column(Integer)
    createtime = Column(DateTime)

    
    def __init__(self, id=None):
        self.id = id
    
    def __repr__(self):
        return '<Name>: %r' % (self.name)

