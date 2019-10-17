from scraper import Scraper
from courses import Courses, Sections
from database import Database

s = Scraper()
courses = {}
courses = s.getData(courses)
db = Database()

db.create_tables()
db.populate(courses)

#     print(course.__dict__)
#     for section in course.sections:
#         print(section.__dict__)
# print(courses)
# print(courses)

# for k, v in courses.items():
#     print(v)
#     for x in v.sections:
#         print(x)
