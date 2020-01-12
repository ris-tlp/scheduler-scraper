import logging
from courseoffering.app import app
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

if __name__ == "__main__":
    app.run(debug=True)