import logging
from datetime import datetime
from scraper.scraper import Scraper
from scraper.database import Database
from multiprocessing.pool import ThreadPool

startTime = datetime.now()

scraper = Scraper()
ThreadPool(5).map(scraper.worker, scraper.terms)

for name, data in scraper.courses.items():
    print(f"{name} : {data}")

db = Database()
db.create_tables()
logging.info("\tTables created")
db.truncate_tables()
logging.info("\tTables truncated")
db.populate(scraper.courses)
logging.info("\tTables populated")

print(f"TOTAL: {datetime.now() - startTime}")
