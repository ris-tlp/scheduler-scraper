from scraper import Scraper

s = Scraper()
courses = []
courses = s.getCourseData(courses)

for course in courses:
    print(course.__dict__)
    for section in course.sections:
        print(section.__dict__)

    print("\n\n")