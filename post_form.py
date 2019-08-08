from courses_list_scrape import returnCourses, returnFormAttributes
from bs4 import BeautifulSoup
import requests

courses = returnCourses()
__VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = returnFormAttributes() 
courseData = {}

for course in courses:
    payload = {
        '__VIEWSTATE': __VIEWSTATE,
        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
        '__EVENTVALIDATION': __EVENTVALIDATION,
        'ctl00$CntntPlcHldr$ddlTerm': '201910',
        'ctl00$CntntPlcHldr$ddlDept': course
        }
    url = "https://registrar.kfupm.edu.sa/CourseOffering"

    response = requests.post(url, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    for row in soup.find_all("div", class_="trow"):
        data.append([]) #creating list of lists of each course

        for inner in row.find_all("div", class_="tdata"):
            index = inner.text.index(":")
            tagContent = inner.text[index+1:] #slicing to get only content
            data[len(data) - 1].append(tagContent) #appending to end of list
    
    courseData[course] = data #setting data according to course abbrev

# output test
for key, value in courseData.items():
    print(f'----------  {key}  ---------- ')
    for _ in value:
        print(_)

print(__VIEWSTATE)
print(__VIEWSTATEGENERATOR)
print(__EVENTVALIDATION)
