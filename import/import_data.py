from base import Base, Session, engine
from courses import Courses
from sections import Sections

Base.metadata.create_all(engine)
session = Session()