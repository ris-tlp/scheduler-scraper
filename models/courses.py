from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from scraper.database import Base


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

    def return_serializable_sections(self):
        """Converts section objects to serializable versions of themselves to allow JSON serialization"""
        serializable_sections = [section.return_serializable_section() for section in self.sections]
        return serializable_sections

    def return_serializable_course(self):
        """Returns a dictionary of the attributes to allow JSON serialization"""
        return {
            "Major": self.major,
            "Term": self.term,
            "Code": self.code,
            "Title": self.title,
            "Sections": self.return_serializable_sections()
        }

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}



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
