from base import Base, Session, engine
from courses import Courses
from sections import Sections
#to import from higher level dir
import sys
sys.path.append("..")

from post_form import getDBData

Base.metadata.create_all(engine)
session = Session()
data = getDBData()

for dept in data:
    for course in dept:
        queryCourses = Courses(
            course["Course"],
            course["Course Name"],
            course["Term"],
            course["Dept"]
        )
        
        querySections = Sections(
            course["Course"],
            course["Instructor"],
            course["Activity"],
            course["Day"],
            course["Loc"].split("-")[0],
            course["Loc"].split("-")[1],
            course["Time"].split("-")[0],
            course["Time"].split("-")[1],
            course["Status"]
        )

        session.add(queryCourses)
        session.add(querySections)
        session.commit()

session.commit()
session.close()