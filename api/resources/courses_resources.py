from flask_restful import Resource
from scraper.database import session
from models.courses import Course
from models.sections import Section
from flask import jsonify


def correctTermFormat(term: str) -> str:
    """Corrects term formats from 192 to 201920"""

    return f"20{term}0" if len(term) != 6 else term


def prepareCoursesDict(courses: dict, course: Course):
    """Creates a key with the course code and removes the same code from the Course object to prevent redundancy"""

    courses[course.code] = course.return_serializable_course()
    del courses[course.code]["Code"]


class CoursesTermAll(Resource):
    """Resource for /courses/<term>/all"""

    def get(self, term):

        courses = {}

        for course in session.query(Course).filter(Course.term == correctTermFormat(term)):
            prepareCoursesDict(courses, course)

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify(courses)


class CoursesTermMajor(Resource):
    """ Resource for /courses/<term>/<major>"""

    def get(self, term, major):

        courses = {}

        for course in session.query(Course).filter(Course.term == correctTermFormat(term), Course.major == major):
            prepareCoursesDict(courses, course)

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify(courses)


class CoursesTermCRN(Resource):
    """Resource for /courses/<term>/<CRN>"""

    def get(self, term, crn):

        courses = {}

        query = session.query(Course).join(Section).filter(
            Section.crn == crn,
            Course.term == correctTermFormat(term)
        )

        prepareCoursesDict(courses, query.first())

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify(courses)


