from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False)
    title = Column(String(length=255), nullable=False)
    term = Column(String(length=255), nullable=False)
    major = Column(String(length=255), nullable=False)
    sections = relationship("Sections")

    def __init__(self, code, title, term, major, sections):
        self.code = code
        self.title = title
        self.term = term
        self.major = major
        self.sections = sections
        
    def __str__(self):
        return (
            f"Major: {self.major}\n"
            f"Term: {self.term}\n"
            f"Code: {self.code}\n"
            f"Title: {self.title}\n"
            f"Sections: {self.sections}\n"
        )

# RAW QUERY
# query = (
#         "CREATE TABLE Courses ("
#         "id INT NOT NULL AUTO_INCREMENT,"
#         "code INT NOT NULL,"
#         "title VARCHAR(255) NOT NULL,"
#         "term VARCHAR(255) NOT NULL,"
#         "major VARCHAR(5) NOT NULL,"
#         "PRIMARY KEY (id));"
#     )



class Sections(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    crn = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
    instructor = Column(String(length=255), nullable=True)
    activity = Column(String(length=255), nullable=False)
    days = Column(String(length=5), nullable=False)
    location = Column(String(length=255), nullable=True)
    start_time = Column(Integer, nullable=False)
    end_time = Column(Integer, nullable=False)
    status = Column(String(length=255), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"))
    courses = relationship("Courses", back_populates="sections")


    def __init__(self, crn, number, instructor, activity, days, location, start_time, end_time, status):
        self.crn = crn
        self.number = number
        self.instructor = instructor
        self.activity = activity
        self.days = days
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.status = status


    def __str__(self):
        return (
            f"Number: {self.number}"
            f"\nCRN:  {self.crn}"
            f"\nInstructor: {self.instructor}"
            f"\nActivity: {self.activity}"
            f"\nDays: {self.days}"
            f"\nLocation: {self.location}"
            f"\nStart time: {self.start_time}"
            f"\nEnd time: {self.end_time}"
            f"\nStatus: {self.status}"
        )
# RAW QUERY
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
