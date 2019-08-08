from bs4 import BeautifulSoup
import requests

url = "https://registrar.kfupm.edu.sa/CourseOffering"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def returnCourses():
    '''Returns a list of all available courses'''

    options = soup.find(id = "CntntPlcHldr_ddlDept")
    courses = []

    for value in options.find_all("option"):
        courses.append(value.get("value"))

    return(courses)

def returnFormAttributes():
    '''Returns form attributes necessary for submission'''

    __VIEWSTATEGENERATOR = soup.find("input", id = "__VIEWSTATEGENERATOR").get("value")
    __VIEWSTATE = soup.find("input", id = "__VIEWSTATE").get("value")
    __EVENTVALIDATION = soup.find("input", id = "__EVENTVALIDATION").get("value")

    return __VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION

def returnLatestTerms():
    '''Returns a list of the 3 most recent terms'''
    
    terms = []
    
    for term in soup.find(id = "CntntPlcHldr_ddlTerm").find_all("option"):
        terms.append(term.get("value"))

    return terms[:3]



if __name__ == "__main__":
    pass