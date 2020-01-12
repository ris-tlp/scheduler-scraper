from flask import Flask
from flask_restful import Resource, Api
from courseoffering.resources.HelloWorld import HelloWorld
from courseoffering.resources.Terms import Terms

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(Terms, '/terms')