import time
import logging
import threading
import multiprocessing

from bs4 import BeautifulSoup
from models.courses import Course
from models.sections import Section
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool

logging.basicConfig(filename="logs.log", level=logging.INFO)
# truncating log file before new run
with open('logs.log', 'w'):
    pass


class Scraper:

    def __init__(self):
        # self.courses = {}
        self.terms = []
        self.departments = []
        # self.threadLocal = threading.local()

        self.chrome = self.getDriver(initial=True)
        self.chrome.get("https://registrar.kfupm.edu.sa/CourseOffering")
        time.sleep(5)

        self.parser = BeautifulSoup(self.chrome.page_source, "html.parser")
        self.setTerms()
        self.setDepartments()
        self.numberCourses = 0

        del self.parser
        self.chrome.quit()

    def getDriver(self, initial=False):
        """
        Generates a new driver for each thread
        :param boolean initial: Only returns a driver, does not set threadLocal attribute if True
        """

        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('start-maximized')

        # if initial:
        return webdriver.Chrome(chrome_options=chrome_options)

        # driver = getattr(self.threadLocal, 'driver', None)
        #
        # if driver is None:
        #     driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/ris/workspace/chromedriver/chromedriver")
        #     setattr(self.threadLocal, 'driver', driver)
        #
        # return driver

    def setTerms(self, limit=2):
        """
        Initializes term with the 3 most recent terms
        """

        for term in self.parser.find(id="CntntPlcHldr_ddlTerm").find_all("option")[:limit]:
            self.terms.append(term.get("value"))

        logging.info(f"Terms acquired: {self.terms}")

    def setDepartments(self):
        """
        Initializes dept with all available departments
        """

        for value in self.parser.find(id="CntntPlcHldr_ddlDept").find_all("option")[1:]:
            self.departments.append(value.get("value"))

        logging.info(f"Depts acquired: {self.departments}")

    def getCourseData(self, row) -> dict:
        """
        Iterates and initializes attributes of ONE course
        """

        data = {}

        for inner in row.find_all("div", class_="tdata"):
            # Some courses are structured with an additional
            # ":" in their name and cause an error
            # when unpacking with just inner.text.split(":").
            # Anything after the first ":" is going to be the
            # value of the attribute, hence maxsplit=1
            key, value = inner.text.split(":", maxsplit=1)
            data[key] = value

        return data


    def getData(self):

        # courses = []
        for term in self.terms:
            self.chrome = self.getDriver()
            self.chrome.get("https://registrar.kfupm.edu.sa/CourseOffering")
            time.sleep(5)
            Select(self.chrome.find_element_by_id("CntntPlcHldr_ddlTerm")).select_by_value(term)

            courses = Pool(multiprocessing.cpu_count() - 1).map(self.worker, self.departments)
            print(courses)
        
        # return courses

    def worker(self, dept):
        """
        Cleanses and scrapes data for a specific term
        :param str term:
        """
        courses = {}
        
        Select(self.chrome.find_element_by_id("CntntPlcHldr_ddlDept")).select_by_value(dept)

        parser = BeautifulSoup(self.chrome.page_source, 'html.parser')


        # Select(chrome.find_element_by_id("CntntPlcHldr_ddlTerm")).select_by_value(term)

        # for term in self.terms:
        #     Select(chrome.find_element_by_id("CntntPlcHldr_ddlTerm")).select_by_value(term)
        #     Select(chrome.find_element_by_id("CntntPlcHldr_ddlDept")).select_by_value(dept)

        #     parser = BeautifulSoup(chrome.page_source, 'html.parser')

        for row in parser.find_all("div", class_="trow"):
            # fetch data of ONE course
            data = self.getCourseData(row)

            # splitting course name and sections
            # as required by the schema
            data["Section"], data["Course"] = (
                data["Course-Sec"].split("-")[1],
                data["Course-Sec"].split("-")[0]
            )

            # Removing space in course code for easier querying
            data["Course"] = "".join(data["Course"].split())

            # splitting Time as start_time and
            # end_time as required by schema
            data["start_time"], data["end_time"] = (
                data["Time"].split("-")[0],
                data["Time"].split("-")[1]
            )

            # setting time as -1 to indicate
            # that the start_time / end_time
            # fields are empty
            if len(data["start_time"]) == 0:
                data["start_time"] = -1

            if len(data["end_time"]) == 0:
                data["end_time"] = -1

            # removing redundant keys
            data.pop("Course-Sec", None)
            data.pop("Time", None)
            self.numberCourses += 1

            # storing name and term of latest course scraped
            # to check whether the previous course that was
            # scraped is the same so as to only append a
            # new section to the course object
            courseID = data["Course"] + term

            section = Section(
                data["CRN"],
                data["Section"],
                data["Instructor"],
                data["Activity"],
                data["Day"],
                data["Loc"],
                data["start_time"],
                data["end_time"],
                data["Status"]
            )

            # If the new course does not already exist, create a new
            # course object and append it to the courses dict,
            # otherwise only create a new section object and
            # append it to courses.sections
            if courseID not in courses:
                sections = [section]

                course = Course(
                    data["Course"],
                    data["Course Name"],
                    term,
                    dept,
                    sections
                )

            else:
                # Only appends the new section of the same course
                courses[courseID].sections.append(section)

            # Set course to unique courseID
            courses[courseID] = course
            logging.info(f"\t {courseID} created")

        time.sleep(2)

        self.chrome.quit()
        return courses

