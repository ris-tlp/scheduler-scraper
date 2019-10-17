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

# TODO: use environment variables for credentials
engine = create_engine("mysql+pymysql://Ajmal:ASDF0987!@localhost/scheduler", echo=True)
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

