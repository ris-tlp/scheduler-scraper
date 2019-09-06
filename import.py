import logging
import requests
import os
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from post_form import getDBData

logging.basicConfig(filename="logs.log", level=logging.INFO)
# Set up database
engine = create_engine("mysql+mysqlconnector://omar:omar@localhost/test")
db = scoped_session(sessionmaker(bind=engine))

# deptData = getDBData()
tables = ["Sections", "Courses"]

def checkTableExists(db, tableName):
    query = (
        "SELECT COUNT(*) "
        "FROM information_schema.tables "
        f"WHERE table_name = '{tableName}';"
    )
    response = db.execute(query)
    db.commit()
    if response.fetchone()[0] == 1:
        return True
    else:
        return False

#FOR TESTING PURPOSES ONLY
# def dropTables(tables: list):
#     for table in tables:
#         db.execute(f"DROP TABLE {table};")
#         db.commit()
#     logging.info("Tables dropped")

# dropTables(tables)

if not checkTableExists(db=db, tableName="Courses"):
    query = (
        "CREATE TABLE Courses ("
        "id INT NOT NULL,"
        "code INT NOT NULL,"
        "title VARCHAR(255) NOT NULL,"
        "term VARCHAR(255) NOT NULL,"
        "major VARCHAR(5) NOT NULL,"
        "PRIMARY KEY (id));"
    )
    db.execute(query)
    db.commit()
    logging.info("CREATED TABLE 'Courses'")

if not checkTableExists(db=db, tableName="Sections"):
    query = (
        "CREATE TABLE Sections ("
        "id INT NOT NULL,"
        "number INT NOT NULL,"
        "instructor VARCHAR(255) NOT NULL,"
        "activity VARCHAR(255) NOT NULL,"
        "days VARCHAR(5) NOT NULL,"
        "bldg VARCHAR(255) NOT NULL,"
        "room VARCHAR(255) NOT NULL,"
        "start_time INT NOT NULL,"
        "end_time INT NOT NULL,"
        "status INT NOT NULL,"
        "course_id INT NOT NULL,"
        "PRIMARY KEY (id),"
        "FOREIGN KEY (course_id) REFERENCES Courses(id));"
    )
    db.execute(query)
    db.commit()
    logging.info("CREATED TABLE 'Sections'")