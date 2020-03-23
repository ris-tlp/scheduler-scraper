from flask import Flask
from flask_restful import Api

from api.resources.courses_resources import (
    CoursesTermAll,
    CoursesTermMajor,
    CoursesTermCRN,
    CoursesTermMajorCNumber,
    CoursesTermMajorCNumberSection
)
from api.resources.terms_resources import Terms

app = Flask(__name__)
api = Api(app)

api.add_resource(Terms, "/terms/", "/terms/<int:limit>")
api.add_resource(CoursesTermAll, "/courses/<string:term>/all")
api.add_resource(CoursesTermMajor, "/courses/<string:term>/<string:major>")
api.add_resource(CoursesTermCRN, "/courses/<string:term>/<int:crn>")
api.add_resource(CoursesTermMajorCNumber, "/courses/<string:term>/<string:major>/<int:courseNumber>")
api.add_resource(CoursesTermMajorCNumberSection, "/courses/<string:term>/<string:major>/<string:courseNumber>/<string:sectionNumber>")