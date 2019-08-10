from bs4 import BeautifulSoup
import requests

url = "https://registrar.kfupm.edu.sa/CourseOffering"

try:
    response = requests.get(url)
except requests.ConnectionError as e:
    print(f"\nError: {e}\n")
    
soup = BeautifulSoup(response.text, 'html.parser')


def getDepartments():
    '''Returns a list of all available departments'''

    options = soup.find(id="CntntPlcHldr_ddlDept")
    depts = []

    for value in options.find_all("option"):
        depts.append(value.get("value"))

    return depts[1:]


def getFormAttributes():
    '''Returns form attributes necessary for submission'''

    __VIEWSTATEGENERATOR = soup.find(
        "input", id="__VIEWSTATEGENERATOR").get("value")
    __VIEWSTATE = soup.find("input", id="__VIEWSTATE").get("value")
    __EVENTVALIDATION = soup.find("input", id="__EVENTVALIDATION").get("value")

    return __VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION


def getTerms(limit=3):
    '''Returns a list of the 3 most recent terms'''

    terms = []

    for term in soup.find(id="CntntPlcHldr_ddlTerm").find_all("option"):
        terms.append(term.get("value"))

    return terms[:limit]


if __name__ == "__main__":
    pass
