from flask_restful import Resource
from courseoffering.utils.database import session
from courseoffering.models.courses import Course
from flask import jsonify


class Courses(Resource):

    def get(self, term):

        # Fetches all terms with corrected Term format (192 -> 201920)
        courses = [course.code for course in session.query(Course).filter(
            Course.term == (f"20{term}0" if len(term) != 6 else term)
        )]

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify({"Courses": courses})
