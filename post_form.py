from courses_list_scrape import returnCourses, returnFormAttributes, returnLatestTerms
from bs4 import BeautifulSoup
import requests

courses = returnCourses()
terms = returnLatestTerms()
__VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = returnFormAttributes()
courseData = {}

for term in terms[:1]:
    for course in courses[:2]:
        payload = {
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': __EVENTVALIDATION,
            'ctl00$CntntPlcHldr$ddlTerm': term,
            'ctl00$CntntPlcHldr$ddlDept': course
        }
        url = "https://registrar.kfupm.edu.sa/CourseOffering"

        response = requests.post(url, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []

        for row in soup.find_all("div", class_="trow"):
            data.append([])  # creating list of lists of each course

            for inner in row.find_all("div", class_="tdata"):
                tagContent = inner.span.next_sibling
                # appending to end of list
                data[len(data) - 1].append(tagContent)

        courseData[course] = data  # setting data according to course abbrev

# output test
# for key, value in courseData.items():
#     print(f' ----------  {key}  ---------- ')
#     for _ in value:
#         print(_)
# print(f'------------------- {term} -------------------')
