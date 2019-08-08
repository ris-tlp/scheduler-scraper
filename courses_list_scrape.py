from bs4 import BeautifulSoup
import requests

def returnCourses():
    url = "https://registrar.kfupm.edu.sa/CourseOffering"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    options = soup.find(id = "CntntPlcHldr_ddlDept")
    courses = []

    for value in options.find_all("option"):
        courses.append(value.get("value"))

    return(courses)

def returnFormAttributes():
    url = "https://registrar.kfupm.edu.sa/CourseOffering"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    __VIEWSTATEGENERATOR = soup.find("input", id = "__VIEWSTATEGENERATOR").get("value")
    __VIEWSTATE = soup.find("input", id = "__VIEWSTATE").get("value")
    __EVENTVALIDATION = soup.find("input", id = "__EVENTVALIDATION").get("value")

    return __VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION


if __name__ == "__main__":
    pass