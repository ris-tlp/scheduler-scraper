from flask_restful import Resource
# from courseoffering.utils.database import Database
# from courseoffering.utils.database import return_terms
# from courseoffering.models.courses import return_terms
from courseoffering.utils.database import session
from courseoffering.models.courses import Course
from flask import jsonify


class Terms(Resource):

    def get(self, limit=None):
        terms = [course.term for course in session.query(Course.term).distinct()]

        if limit is None:
            return jsonify({
                "Terms": terms
            })
        else:
            return jsonify({
                "Terms": terms[:limit]
            })
