from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# TODO: use environment variables for credentials
engine = create_engine("mysql+pymysql://username:password@localhost/test", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
    
Session = sessionmaker(bind=engine)
Base = declarative_base()