from scraper import Scraper
from courses import Courses, Sections

s = Scraper()
courses = {}
courses = s.getData(courses)


#     print(course.__dict__)
#     for section in course.sections:
#         print(section.__dict__)
# print(courses)
# print(courses)

for k, v in courses.items():
    for x in v.sections:
        print(x)
