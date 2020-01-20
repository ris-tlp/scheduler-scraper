from flask import Flask
from flask_restful import Resource, Api
from courseoffering.resources.terms import Terms
from courseoffering.resources.courses import CoursesTermAll, CoursesTermMajor, CoursesTermCRN

app = Flask(__name__)
api = Api(app)

api.add_resource(Terms, "/terms/", "/terms/<int:limit>")
api.add_resource(CoursesTermAll, "/courses/<string:term>/all")
api.add_resource(CoursesTermMajor, "/courses/<string:term>/<string:major>")
api.add_resource(CoursesTermCRN, "/courses/<string:term>/<int:crn>")

