import unittest
import requests
from bs4 import BeautifulSoup
from courses_list_scrape import getDepartments, getFormAttributes, getTerms

url = "https://registrar.kfupm.edu.sa/CourseOffering"
__VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = getFormAttributes()
payload = {
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': __EVENTVALIDATION,
            'ctl00$CntntPlcHldr$ddlTerm': getTerms(limit=1),
            'ctl00$CntntPlcHldr$ddlDept': "ICS"
        }
response = requests.post(url, data=payload)
soup = BeautifulSoup(response.text, 'html.parser')

class Tests(unittest.TestCase):

    def testResponseIsNotNone(self):
        self.assertIsNotNone(response)
    
    def testAttributesIsNotNone(self):
        __VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = getFormAttributes()
        self.assertIsNotNone(__VIEWSTATE)
        self.assertIsNotNone(__VIEWSTATEGENERATOR)
        self.assertIsNotNone(__EVENTVALIDATION)

    def testDeptsIsNotNone(self):
        depts = getDepartments()
        self.assertIsNotNone(depts)

    def testTermsIsNotNone(self):
        terms = getTerms()
        self.assertIsNotNone(terms)

    def testFormStructure(self):
        self.assertIsNotNone(soup.find(id="CntntPlcHldr_ddlDept"))
        self.assertIsNotNone(soup.find(id="CntntPlcHldr_ddlTerm"))
        #list will be false if empty
        self.assertTrue(soup.find(id="CntntPlcHldr_ddlTerm").find_all("option"))
        self.assertTrue(soup.find(id="CntntPlcHldr_ddlDept").find_all("option"))
    
    def testDataTableStructure(self):
        #list will be false if empty
        self.assertTrue(soup.find_all("div", class_="trow"))
        self.assertTrue(soup.find_all("div", class_="tdata"))
        


if __name__ == "__main__":
    unittest.main()
        