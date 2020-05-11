from datetime import datetime

from scraper.database import Database
from scraper.scraper import Scraper
import logging


startTime = datetime.now()


scraper = Scraper()
courses = scraper.getData({})

for name, data in courses.items():
    print(f"{name} : {data}")

scraper.chrome.quit()

db = Database()
db.create_tables()
logging.info("\tTables created")
db.truncate_tables()
logging.info("\tTables truncated")
db.populate(courses)
logging.info("\tTables populated")

print(f"TOTAL: {datetime.now() - startTime}")