from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False)
    title = Column(String(length=255), nullable=False)
    term = Column(String(length=255), nullable=False)
    major = Column(String(length=255), nullable=False)
    # sections = relationship("Sections")

    def __init__(self, code, title, term, major):
        self.code = code
        self.title = title
        self.term = term
        self.major = major

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