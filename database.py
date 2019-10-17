from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database

# TODO: use environment variables for credentials
engine = create_engine("mysql+pymysql://omar:omar@localhost/test", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
    
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
meta = MetaData()

class Database():
    '''Handles all operations that concerns Databases'''
    
    def create_tables(self):
        '''Initially create tables in the Database'''
        
        courses = Table(
            "courses", meta,
                Column("id", Integer, primary_key=True),
                Column("code", String(length=255), nullable=False),
                Column("title", String(length=255), nullable=False),
                Column("term", String(length=255), nullable=False),
                Column("major", String(length=255), nullable=False),
                # relationship("Sections", backref="Courses")
        )
        
        sections = Table(
            "sections", meta,
                Column("id", Integer, primary_key=True),
                Column("crn", Integer, nullable=False),
                Column("number", String(length=255), nullable=False),
                Column("instructor", String(length=255), nullable=True),
                Column("activity", String(length=255), nullable=False),
                Column("days", String(length=5), nullable=True),
                Column("location", String(length=255), nullable=True),
                Column("start_time", Integer, nullable=True),
                Column("end_time", Integer, nullable=True),
                Column("status", String(length=255), nullable=False),
                Column("course_id", Integer, ForeignKey("courses.id"))
        )
        
        meta.create_all(engine)

    def populate(self, courseData: dict):    
        '''Initially populate the tables with data'''    
        
        for course, data in courseData.items():
            session.add(data)
            session.commit()
        