import unittest
import requests
from bs4 import BeautifulSoup
from scraper import Scraper

scraper = Scraper()
scraper.setTerms(2)
scraper.setDepartments()
scraper.setFormAttributes()

payload = scraper.getPayload(scraper.terms, scraper.depts)
response = requests.post(scraper.url, data=payload)
soup = BeautifulSoup(response.text, 'html.parser')


class Tests(unittest.TestCase):

    def test_response_is_not_none(self):
        self.assertIsNotNone(response)
    
    def test_depts_is_not_none(self):
        self.assertIsNotNone(scraper.depts)

    def test_terms_is_not_none(self):
        self.assertIsNotNone(scraper.terms)

    def test_form_structure(self):
        self.assertIsNotNone(soup.find(id="CntntPlcHldr_ddlDept"))
        self.assertIsNotNone(soup.find(id="CntntPlcHldr_ddlTerm"))
        #list will be false if empty
        self.assertTrue(soup.find(id="CntntPlcHldr_ddlTerm").find_all("option"))
        self.assertTrue(soup.find(id="CntntPlcHldr_ddlDept").find_all("option"))
    
    def test_data_table_structure(self):
        #list will be false if empty
        self.assertTrue(soup.find_all("div", class_="trow"))
        self.assertTrue(soup.find_all("div", class_="tdata"))


if __name__ == "__main__":
    unittest.main()
        