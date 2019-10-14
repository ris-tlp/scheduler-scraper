from scraper import Scraper
from courses import Course

s = Scraper()
courses = {}
courses = s.getData(courses)


#     print(course.__dict__)
#     for section in course.sections:
#         print(section.__dict__)
# print(courses)
print(courses["AE  402201910"])
for x in courses["AE  402201910"].sections:
    print(x)
    print("\n\n")


