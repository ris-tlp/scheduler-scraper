import requests
import os
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from post_form import getDBData

# Set up database
engine = create_engine("mysql+mysqlconnector://omar:omar@localhost/test")
db = scoped_session(sessionmaker(bind=engine))
print(engine)
# deptData = getDBData

