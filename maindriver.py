import logging 
from scraper import Scraper
from database import Database
from models.courses import Course
from models.sections import Section

s = Scraper()
courses = {}
courses = s.getData(courses)
db = Database()

db.create_tables()
logging.info("\tTables created")
db.truncate_tables()
logging.info("\tTables truncated")
db.populate(courses)
logging.info("\tTables populated")
