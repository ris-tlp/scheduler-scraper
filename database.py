from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database
import json


with open("credentials.json", "r") as read_file:
    data = json.load(read_file)

engine = create_engine(
    f"mysql+pymysql://{data['user']}:{data['password']}@localhost/{data['database']}",
    echo = True
)

if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
meta = MetaData()


class Database:
    """Handles all operations that concerns Databases"""

    def create_tables(self):
        """Initially create tables in the Database"""

        Base.metadata.create_all(engine)

    def populate(self, courseData: dict):
        """Initially populate the tables with data"""

        courselist = list(courseData.values())
        session.add_all(courselist)
        session.commit()

    def truncate_tables(self):
        """Trunactes sections and courses tables in the database"""

        session.execute("""TRUNCATE TABLE sections""")
        session.execute("""SET FOREIGN_KEY_CHECKS = 0""")
        session.execute("""TRUNCATE TABLE courses""")
        session.execute("""SET FOREIGN_KEY_CHECKS = 1""")
