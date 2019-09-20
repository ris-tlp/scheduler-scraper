class Course:
    """
    Stores attributes that are unique to a single course.
    A single course can have multiple sections.
    """

    def __init__(self, major, term, code, title, sections: list):
        self.major = major
        self.term = term
        self.code = code
        self.title = title
        self.sections = sections

    def __str__(self):
        return (
            f"Major: {self.major}\n"
            f"Term: {self.term}\n"
            f"Code: {self.code}\n"
            f"Title: {self.title}\n"
            f"Sections: {self.sections}\n"
        )


class Section:
    """
    Stores attributes that are unique to a single section.
    A single question can only have a single course.
    """

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

    def __str__(self):
        return (
            f"Number: {self.number}"
            f"CRN:  {self.crn}"
            f"Instructor: {self.instructor}"
            f"Activity: {self.activtiy}"
            f"Days: {self.days}"
            f"Building: {self.bldg}"
            f"Room: {self.room}"
            f"Start time: {self.start_time}"
            f"End time: {self.end_time}"
            f"Status: {self.status}"
        )
