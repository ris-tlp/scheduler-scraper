from scraper import Scraper
from courses import Courses, Sections
from database import Database
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

#     print(course.__dict__)
#     for section in course.sections:
#         print(section.__dict__)
# print(courses)
# print(courses)

# for k, v in courses.items():
#     print(v)
#     for x in v.sections:
#         print(x)
