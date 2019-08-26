from courses_list_scrape import getDepartments, getFormAttributes, getTerms
from bs4 import BeautifulSoup
import requests
import logging
from datetime import datetime
import time

logging.basicConfig(filename="logs.log", level=logging.INFO)

depts = getDepartments()
terms = getTerms()
__VIEWSTATEGENERATOR, __VIEWSTATE, __EVENTVALIDATION = getFormAttributes()
deptData = {}
startTime = datetime.now()  # to log script execution time
logging.info(f"Script execution started: {startTime}")
# session to reuse the same TCP connection accross requests
session = requests.Session()

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
            response = session.post(url, data=payload)
        except requests.RequestException as e:
            logging.error(e)

        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        numberOfCourses = 0

        for row in soup.find_all("div", class_="trow"):
            data.append([])  # creating list of lists of each course

            for inner in row.find_all("div", class_="tdata"):
                # splitting to get only content
                tagContent = inner.text.split(":")[1]
                # appending to end of list
                data[len(data) - 1].append(tagContent)

            numberOfCourses += 1

        logging.info(f"{numberOfCourses} {dept} courses scraped")
        deptData[dept] = data  # setting data according to course abbrev
        time.sleep(5)

totalTime = datetime.now() - startTime
logging.info(f"Total script execution time: {totalTime}")

# output test
# print(deptData)
# for key, value in deptData.items():
#     print(f' ----------  {key}  ---------- ')
#     for _ in value:
#         print(_)
# print(f'------------------- {term} -------------------')
