import json

from flask_restful import Resource
from courseoffering.utils.database import session
from courseoffering.models.courses import Course
from courseoffering.models.sections import Section
from flask import jsonify
from sqlalchemy.ext.serializer import loads, dumps


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

        # courses = [course.return_serializable_course() for course in session.query(Course).filter(
        #     Course.term == correctTermFormat(term)
        # )]

        # courses = {course.code: course.return_serializable_course() for course in session.query(Course).filter(
        #     Course.term == correctTermFormat(term)
        # )}

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

        # courses = [course.return_serializable_course() for course in session.query(Course).filter(
        #     Course.term == correctTermFormat(term),
        #     Course.major == major
        # )]

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
        result = session.query(Course).join(Section).filter(
            Section.crn == crn,
            Course.term == correctTermFormat(term)
        )

        courses = [course.as_dict() for course in result]
        print(courses)


        # print(courses)
        # ncourses = {course["code"]: course for course in courses}

        if not courses:
            return jsonify({"Courses": "None"})
        else:
            return jsonify({"Courses": courses})


