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

if __name__ == "__main__":
    pass