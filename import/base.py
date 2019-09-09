from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://omar:omar@localhost/test")
Session = sessionmaker(bind=engine)
Base = declarative_base()