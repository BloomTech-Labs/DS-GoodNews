import sqlite3
from urllib.request import pathname2url

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