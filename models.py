from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapper, relationship
from database import Base 

class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.id'))
    keyword = Column(String)

    def __init__(self, id=None):
        self.id = id


class Story(Base):

    __tablename__ = "stories"

    id = Column(Integer, primary_key = True)
    name = Column(String(256))
    imageurl = Column(String(1024))
    url = Column(String(1024))
    timestamp = Column(DateTime)
    description = Column(String())
    keywords = relationship('Keyword')
    summary = Column(String())
    content = Column(String())
    clickbait = Column(Integer)
    createtime = Column(DateTime)

    
    def __init__(self, id=None):
        self.id = id
    
    # def __repr__(self):
    #     return '<Name: %r' % (self.name)

