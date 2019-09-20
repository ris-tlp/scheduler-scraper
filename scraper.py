from courses import Course, Section
from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(filename="logs.log", level=logging.INFO)


class Scraper():

    def __init__(self):
        self.depts = []
        self.terms = []
        self.__VIEWSTATEGENERATOR = ""
        self.__EVENTVALIDATION = ""
        self.__VIEWSTATE = ""
        self.url = "https://registrar.kfupm.edu.sa/CourseOffering"
        self.session = requests.Session()

        try:
            response = self.session.get(self.url)
        except requests.RequestException as e:
            logging.error(e)

        self.soup = BeautifulSoup(response.text, 'html.parser')

    def setDepartments(self):
        '''Initializes dept with all available departments'''

        options = self.soup.find(id="CntntPlcHldr_ddlDept")

        for value in options.find_all("option"):
            self.depts.append(value.get("value"))      

    def setFormAttributes(self):
        '''Initializes form attributes necessary for submission'''

        self.__VIEWSTATEGENERATOR = self.soup.find(
            "input", id="__VIEWSTATEGENERATOR").get("value")
        self.__VIEWSTATE = self.soup.find(
            "input", id="__VIEWSTATE").get("value")
        self.__EVENTVALIDATION = self.soup.find(
            "input", id="__EVENTVALIDATION").get("value")

    def setTerms(self, limit=3):
        '''Initializes term with the 3 most recent terms'''

        # for term in self.soup.find(id="CntntPlcHldr_ddlTerm").find_all("option"):
        #     self.terms.append(term.get("value"))

        [
            self.terms.append(term.get("value"))
            for term
            in self.soup.find(id="CntntPlcHldr_ddlTerm").find_all("option")
        ]

        self.terms = self.terms[:limit]

    def getCourseData(self, courses: list) -> list:
        """
        Scrapes the KFUPM Course offering page and returns a
        courses list containing course objects
        """

        # Initializing necessary attributes
        self.setTerms()
        self.setDepartments()
        self.setFormAttributes()

        for term in self.terms[:2]:
            logging.info(term)
            for dept in self.depts[:4]:

                payload = {
                    '__VIEWSTATE': self.__VIEWSTATE,
                    '__VIEWSTATEGENERATOR': self.__VIEWSTATEGENERATOR,
                    '__EVENTVALIDATION': self.__EVENTVALIDATION,
                    'ctl00$CntntPlcHldr$ddlTerm': term,
                    'ctl00$CntntPlcHldr$ddlDept': dept
                }

                try:
                    response = self.session.post(self.url, data=payload)
                except requests.RequestException as e:
                    logging.error(e)

                soup = BeautifulSoup(response.text, 'html.parser')
                data = []
                numberOfCourses = 0
                previousCourse = None

                for row in soup.find_all("div", class_="trow"):
                    # creates a new dictionary to store the
                    # attributes of a course
                    data.append({})

                    # iterates through attributes of ONE course
                    for inner in row.find_all("div", class_="tdata"):
                        # setting up dictionary with keys & values
                        data[len(data) - 1][inner.text.split(":")[0]] = inner.text.split(":")[1]
                        # splitting course name and sections
                        # as required by the schema
                        data[len(data) - 1]["Section"], data[len(data) - 1]["Course"] = (
                            data[len(data) - 1]["Course-Sec"].split("-")[1],
                            data[len(data) - 1]["Course-Sec"].split("-")[0]
                        )

                    numberOfCourses += 1
                    # removing redundant key
                    data[len(data) - 1].pop("Course-Sec", None)

                    # storing name of latest course scraped
                    # to check whether the previous course that was
                    # scraped is the same so as to only append a
                    # new section to the course object
                    currentCourse = data[len(data) - 1]["Course"]

                    # If the previous course is not the same as
                    # the course scraped next, create a new
                    # course object and append it to the courses list,
                    # otherwise only create a new section object and
                    # append it to courses.sections
                    if (previousCourse is None) or (previousCourse != currentCourse):
                        section = Section(
                            data[len(data) - 1]["Section"],
                            data[len(data) - 1]["CRN"],
                            data[len(data) - 1]["Instructor"],
                            data[len(data) - 1]["Activity"],
                            data[len(data) - 1]["Day"],
                            data[len(data) - 1]["Loc"].split("-")[0],
                            data[len(data) - 1]["Loc"].split("-")[1],
                            data[len(data) - 1]["Time"].split("-")[0],
                            data[len(data) - 1]["Time"].split("-")[1],
                            data[len(data) - 1]["Status"]
                        )
                        
                        sections = []
                        sections.append(section)

                        course = Course(
                            dept,
                            term,
                            data[len(data) - 1]["Course"],
                            data[len(data) - 1]["Course Name"],
                            sections
                        )

                        # Changing the previous course so as to indicate
                        # that a new course object must be created
                        previousCourse = currentCourse

                    else:
                        section = Section(
                            data[len(data) - 1]["Section"],
                            data[len(data) - 1]["CRN"],
                            data[len(data) - 1]["Instructor"],
                            data[len(data) - 1]["Activity"],
                            data[len(data) - 1]["Day"],
                            data[len(data) - 1]["Loc"].split("-")[0],
                            data[len(data) - 1]["Loc"].split("-")[1],
                            data[len(data) - 1]["Time"].split("-")[0],
                            data[len(data) - 1]["Time"].split("-")[1],
                            data[len(data) - 1]["Status"]
                        )

                        # Only appends the new section of the same course
                        # to courses.section
                        courses[len(courses) - 1].sections.append(section)

                    courses.append(course)

        return courses
