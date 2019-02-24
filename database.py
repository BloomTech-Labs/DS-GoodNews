import sqlite3
from urllib.request import pathname2url
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

database_url = os.getenv('DATABASE_URL')
engine = create_engine(database_url, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
autoflush = False,
bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

class Database:

    def __init__(self, name):
        self.name = name

    def connect(self):

        try:
            dburi = 'file:{}?mode=rw'.format(pathname2url(self.name))
            self.conn = sqlite3.connect(dburi, uri=True)
        except:
            self.conn = sqlite3.connect(self.name)
            cursor = self.conn.cursor()
            cursor.execute('''
            create table stories (
            id TEXT,
            name TEXT,
            imageurl TEXT,
            url TEXT,
            timestamp TEXT,
            description TEXT,
            keywords TEXT,
            summary TEXT,
            content TEXT,
            clickbait INTEGER,
            createtime  TEXT
            );
            ''')
            cursor.execute('''
            create table keywords (
                story_id TEXT,
                keyword TEXT
            );
            ''')
            self.conn.commit()

    def insert(self,stories, keywords):
        self.conn.executemany("INSERT INTO stories VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", stories)
        self.conn.executemany("INSERT INTO keywords VALUES (?, ?)", keywords)
        self.conn.commit()
        self.conn.close()

    def read(self):
       c = self.conn.execute("SELECT * FROM stories")
       return c.fetchall()