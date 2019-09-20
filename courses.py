class Course:

    def __init__(self, major, term, code, title, sections):
        self.major = major
        self.term = term
        self.code = code
        self.title = title
        self.sections = sections

class Section:

    def __init__(self, number, crn, instructor, activity, days, bldg, room, start_time, end_time, status):
        self.number = number
        self.crn = crn
        self.instructor = instructor
        self.activtiy = activity
        self.days = days
        self.bldg = bldg
        self.room = room
        self.start_time = start_time
        self.end_time = end_time
        self.status = status