import unittest
import requests
from courses_list_scrape import getDepartments, getFormAttributes, getTerms

class Tests(unittest.TestCase):

    def testResponseIsNotNone(self):
        url = "https://registrar.kfupm.edu.sa/CourseOffering"
        response = requests.get(url)
        self.assertIsNotNone(response)

    def testDeptsIsNotNone(self):
        depts = getDepartments()
        self.assertIsNotNone(depts)
    
    def testAttributesIsNotNone(self):
        __VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = getFormAttributes()
        self.assertIsNotNone(__VIEWSTATE)
        self.assertIsNotNone(__VIEWSTATEGENERATOR)
        self.assertIsNotNone(__EVENTVALIDATION)

    def testTermsIsNotNone(self):
        terms = getTerms()
        self.assertIsNotNone(terms)


if __name__ == "__main__":
    unittest.main()
        