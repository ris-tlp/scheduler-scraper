from courses_list_scrape import getDepartments, getFormAttributes, getTerms
from bs4 import BeautifulSoup
import requests

depts = getDepartments()
terms = getTerms()
__VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = getFormAttributes()
deptData = {}

for term in terms:
    for dept in depts:
        payload = {
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': __EVENTVALIDATION,
            'ctl00$CntntPlcHldr$ddlTerm': term,
            'ctl00$CntntPlcHldr$ddlDept': dept
        }
        url = "https://registrar.kfupm.edu.sa/CourseOffering"

        try:
            response = requests.get(url)
        except requests.ConnectionError as e:
            print(f"Error: {e}\n")

        soup = BeautifulSoup(response.text, 'html.parser')
        data = []

        for row in soup.find_all("div", class_="trow"):
            data.append([])  # creating list of lists of each course

            for inner in row.find_all("div", class_="tdata"):
                # splitting to get only content
                tagContent = inner.text.split(":")[1]
                # appending to end of list
                data[len(data) - 1].append(tagContent)

        deptData[dept] = data  # setting data according to course abbrev

# output test

for key, value in deptData.items():
    print(f' ----------  {key}  ---------- ')
    for _ in value:
        print(_)
print(f'------------------- {term} -------------------')

