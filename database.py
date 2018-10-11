import sqlite3
from urllib.request import pathname2url
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://futwbmvbyrhtef:03951d4002b008dd22cf37056918a89f74ca277d930c697ca695a73b157aae19@ec2-54-227-241-179.compute-1.amazonaws.com:5432/dborn2t2u1gaii', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
autoflush = False,
bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

