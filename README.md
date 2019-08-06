# kfupm-course-scraper

## courses_list_scrape.py
Gets the name of all the majors avaiable on the CourseOffering page to pass on to the form to get further information about courses. Returns a list of all the majors in their abbreviation form as required by the form.  
  
## post_form.py
Uses the list returned from `courses_list_scrape.py` to gather information about courses available for each and every major.
Returns a dictionary which contains the name of majors as a key and a list of lists of all the courses available.

`python3 -m pip install pipenv`  
`pipenv install` to install dependencies  
`pipenv shell`  
Uncomment the "output test" lines if you want to see the output and `python3 post_form.py`  

## Sample output
```
----------  CEM  ---------- 
['CEM 510-01', 'LEC', '10103', 'Project Planning & Scheduling', 'ADEL ALSHIBANI', 'UT', '1720-1835', '19-301', 'Open']
['CEM 511-01', 'LEC', '17242', 'Construction Estimating', 'ALI SHASH', 'UT', '1845-2000', '19-410', 'Open']
['CEM 512-01', 'LEC', '18607', 'Value Engineering', ' ', 'UT', '1845-2000', '19-301', 'Open']
['CEM 515-01', 'LEC', '16076', 'Project Quality Management', 'FIRAS TUFFAHA', 'MW', '1845-2000', '19-401', 'Open']
['CEM 520-01', 'LEC', '15537', 'Construction Contracting & Administration', 'ABDULAZIZ BU-BUSHAIT', 'MW', '1720-1835', '19-401', 'Open']
['CEM 525-01', 'LEC', '17245', 'Project Delivery Systems', 'ALI SHASH', 'UT', '1720-1835', '19-424', 'Open']
['CEM 530-01', 'LEC', '15689', 'Construct Engineering', 'ADEL ALSHIBANI', 'UT', '1845-2000', '19-424', 'Open']
['CEM 599-01', 'SEM', '10111', 'Research Seminar', 'LAITH HADIDI', 'T', '2010-2100', '19-424', 'Open']
['CEM 600-01', 'MR', '11940', 'Master of Engineering Report', ' ', '', '-', '-', 'Open']
['CEM 600-02', 'MR', '16237', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['CEM 610-01', 'THS', '11946', 'Thesis', 'KHALAF AL-OFI', '', '-', '-', 'Open']
['EM  510-01', 'LEC', '14623', 'Engineering Economy', 'LAITH HADIDI', 'UT', '1845-2000', '19-401', 'Open']
['EM  510-02', 'LEC', '16426', 'Engineering Economy', 'LAITH HADIDI', 'MW', '1720-1835', '19-301', 'Open']
['EM  520-01', 'LEC', '14126', 'Quantitative Methods in Engineering Management', 'GHAITHAN AHMED', 'UT', '1845-2000', '19-418', 'Open']
['EM  520-02', 'LEC', '16427', 'Quantitative Methods in Engineering Management', 'GHAITHAN AHMED', 'MW', '1845-2000', '19-301', 'Open']
['EM  530-01', 'LEC', '14624', 'Decision Analysis', 'FIRAS TUFFAHA', 'MW', '1720-1835', '19-410', 'Open']
['EM  550-01', 'LEC', '15539', 'Project Management', 'ABDULAZIZ BU-BUSHAIT', 'MW', '1845-2000', '19-424', 'Closed']
['EM  599-01', 'SEM', '15108', 'Research Seminar', 'LAITH HADIDI', 'T', '2010-2100', '19-424', 'Open']
['EM  600-01', 'MR', '15540', 'Master of Engineering Report', ' ', '', '-', '-', 'Open']
['EM  600-02', 'MR', '16238', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['EM  600-03', 'MR', '16239', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['EM  600-04', 'MR', '16240', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['EM  600-05', 'MR', '16241', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['EM  600-06', 'MR', '16242', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['EM  600-07', 'MR', '16243', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
['EM  600-08', 'MR', '16244', 'Master of Engineering Report', ' ', '', '-', '-', 'Closed']
```

