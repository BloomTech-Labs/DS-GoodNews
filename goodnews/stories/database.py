import sqlite3
from urllib.request import pathname2url

def connect():

    try:
        dburi = 'file:{}?mode=rw'.format(pathname2url('goodnews.db'))
        conn = sqlite3.connect(dburi, uri=True)
    except:
        conn = sqlite3.connect('goodnews.db')
        cursor = conn.cursor()
        cursor.execute('''
        create table stories (
        id TEXT,
        name TEXT,
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
        conn.commit()

    return conn

def insert(conn, stories, keywords):
    conn.executemany("INSERT INTO stories VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", stories)
    conn.executemany("INSERT INTO keywords VALUES (?, ?)", keywords)
    conn.commit()
    conn.close()
    return 0


