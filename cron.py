from scraper.database import Database
from scraper.scraper import Scraper
import logging


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
