from flask_restful import Resource
from courseoffering.utils.database import session
from courseoffering.models.courses import Course
from courseoffering.models.sections import Section
from flask import jsonify


def correctTermFormat(term: str) -> str:
    """Corrects term formats from 192 to 201920"""
    return f"20{term}0" if len(term) != 6 else term


class CoursesTermAll(Resource):
    """Resource for /courses/<term>/all"""

    def get(self, term):

        courses = [course.return_serializable_course() for course in session.query(Course).filter(
            Course.term == correctTermFormat(term)
        )]

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify({"Courses": courses})


class CoursesTermMajor(Resource):
    """ Resource for /courses/<term>/<major>"""

    def get(self, term, major):

        courses = [course.return_serializable_course() for course in session.query(Course).filter(
            Course.term == correctTermFormat(term),
            Course.major == major
        )]

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify({"Courses": courses})


class CoursesTermCRN(Resource):
    """Resource for /courses/<term>/<CRN>"""

    def get(self, term, crn):

        courses = [course.return_serializable_course() for course in session.query(Course).join(Section).filter(
            Section.crn == crn,
            Course.term == correctTermFormat(term)
        )]

        if not courses:
            return jsonify({"Courses:" "None"})
        else:
            return jsonify({"Courses": courses})


