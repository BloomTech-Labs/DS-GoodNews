from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.schema import UniqueConstraint
from database import Base 
from collections import OrderedDict

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.id'))
    clickbait = Column(Boolean)
    voter_id = Column(String)
    __table_args__ = (UniqueConstraint('story_id', 'voter_id',name='_voter_story_uc'),
                     )
    def __init__(self, voter_id = None):
        self.voter_id = voter_id

    def __repr__(self):
        return '<ClickBait>:%r' % (self.clickbait)


class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.id'), index=True)
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
    url = Column(String(1024), index=True, unique=True)
    timestamp = Column(DateTime, index=True)
    description = Column(String())
    keywords = relationship("Keyword")
    votes = relationship("Vote")
    summary = Column(String())
    content = Column(String())
    clickbait = Column(Integer)
    createtime = Column(DateTime)

    
    def __init__(self, id=None):
        self.id = id
    
    def __repr__(self):
        return '<Name>: %r' % (self.name)

    def to_dict(self):
        article_dictionary = OrderedDict([
            ("id" , self.id),
            ("name", self.name),
            ("imageurl", self.imageurl),
            ("url" , self.url),
            ("timestamp" , self.timestamp.isoformat() if self.timestamp is not None else ""),
            ("description" , self.description),
            ("keywords" , [k.keyword for k in self.keywords]),
            ("summary" , self.summary),
            ("content" , self.content),
            ("clickbait" , self.clickbait),
            ("createtime" , self.createtime.isoformat() if self.createtime is not None else "")
        ])
        return article_dictionary

class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key = True)
    name = Column(String(256))  
    url = Column(String(1024))

    def __init__(self, url=None):
        self.url = url
    
    def __repr__(self):
        return '<URL>: %r' % (self.url)
