import logging
from datetime import datetime
from scraper.scraper import Scraper
from scraper.database import Database

startTime = datetime.now()

scraper = Scraper()
# courses = ThreadPool(5).map(scraper.worker, scraper.terms)
# courses = Pool(multiprocessing.cpu_count() - 1).map(scraper.worker, scraper.departments)
courses = scraper.getData()

# for name, data in scraper.courses.items():
#     print(f"{name} : {data}")

# print(courses)

# print(f"Number of courses: {scraper.numberCourses}")

# db = Database()
# db.create_tables()
# logging.info("\tTables created")
# db.truncate_tables()
# logging.info("\tTables truncated")
# db.populate(scraper.courses)
# logging.info("\tTables populated")

print(f"TOTAL: {datetime.now() - startTime}")
