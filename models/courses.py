from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String(length=255), nullable=False)
    title = Column(String(length=255), nullable=False)
    term = Column(String(length=255), nullable=False)
    major = Column(String(length=255), nullable=False)
    sections = relationship("Section", backref="Course")

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
#         "code VARCHAR(255) NOT NULL,"
#         "title VARCHAR(255) NOT NULL,"
#         "term VARCHAR(255) NOT NULL,"
#         "major VARCHAR(5) NOT NULL,"
#         "PRIMARY KEY (id));"
#     )
