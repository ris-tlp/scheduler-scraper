from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Sections(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    instructor = Column(String(length=255), nullable=False)
    activity = Column(String(length=255), nullable=False)
    days = Column(String(length=5), nullable=False)
    building = Column(String(length=255), nullable=False)
    room = Column(String(length=255), nullable=False)
    start_time = Column(Integer, nullable=False)
    end_time = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)


    def __init__(self, id, number, instructor, activity, days, building, room, start_time, end_time, status, course_id):
        self.id = id
        self.number = number
        self.instructor = instructor
        self.activity = activity
        self.days = days
        self.building = building
        self.room = room
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.course_id = course_id


#   query = (
#         "CREATE TABLE Sections ("
#         "id INT NOT NULL AUTO_INCREMENT,"
#         "number INT NOT NULL,"
#         "instructor VARCHAR(255) NOT NULL,"
#         "activity VARCHAR(255) NOT NULL,"
#         "days VARCHAR(5) NOT NULL,"
#         "bldg VARCHAR(255) NOT NULL,"
#         "room VARCHAR(255) NOT NULL,"
#         "start_time INT NOT NULL,"
#         "end_time INT NOT NULL,"
#         "status INT NOT NULL,"
#         "course_id INT NOT NULL,"
#         "PRIMARY KEY (id),"
#         "FOREIGN KEY (course_id) REFERENCES Courses(id));"