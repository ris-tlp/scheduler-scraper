from flask import Flask
from flask_restful import Resource, Api
from courseoffering.resources.terms import Terms
from courseoffering.resources.courses import Courses

app = Flask(__name__)
api = Api(app)

api.add_resource(Terms, "/terms/", "/terms/<int:limit>")
api.add_resource(Courses, "/courses/<string:term>/all")

