import logging
from courseoffering.app import app
from flask_script import Manager
from courseoffering.utils.database import Database
from courseoffering.utils.scraper import Scraper

#
# s = Scraper()
# courses = {}
# courses = s.getData(courses)
#
# db = Database()
# db.create_tables()
# logging.info("\tTables created")
# db.truncate_tables()
# logging.info("\tTables truncated")
# db.populate(courses)
# logging.info("\tTables populated")

manager = Manager(app)


@manager.command
def run():
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
