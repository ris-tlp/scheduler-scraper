# kfupm-course-scraper

## scraper.py
`Scraper` class that handles the scraping of the CourseOfferings page. Returns a `courses` list that contains objects of the `Course` class.   
  
## courses.py
Contains `Course` and `Section` classes that store data scraped from the `Scraper` class.  

## maindriver.py
Gathers data from `scraper.py` and other places that haven't been implemented yet man why am I writing this so useless but looks neat af tho gg  

`python3 -m pip install pipenv` to install the pip virtual environment.  
`pipenv install`  to install dependencies from the pipfile.  
`pipenv shell`  to activate the virtual environment.  