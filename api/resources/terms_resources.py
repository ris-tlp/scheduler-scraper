from scraper.database import session
from flask import jsonify
from flask_restful import Resource

from models.courses import Course


class Terms(Resource):
    """Resource for /terms/[limit]"""

    def get(self, limit=None):
        terms = [course.term for course in session.query(Course.term).distinct()]

        if limit is None:
            return jsonify({"Terms": terms})
        else:
            return jsonify({"Terms": terms[:limit]})
