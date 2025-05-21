# Hi everyone! 

I am Anastasia, and here are some comments about the Test.

# Task 1. 
> Describe the steps for comprehensively testing of a pencil with an eraser on one end. Cases for all types of testing (such as functional, usability, performance, load, stress, security, etc.) are expected here.

You can find the detailed answer in [tests/task01.md](tests/task01.md)

# Task 2. 
> On the Main page of https://www.hepsiburada.com/ you can see the different Recommendations section with different products. These sections are also shown on Product Detail and Cart pages. What are these product suggestions, what is the rule for listing these products and showing them to the user? Full analysis is expected here.

You can find the detailed answer in [tests/task02.md](tests/task02.md)

# Task 3 
> Automate the scenario below:
```
1. Visit https://useinsider.com/ and check Insider home page is opened or not
2. Select “Company” menu in navigation bar, select “Careers” and check Career
page, its Locations, Teams and Life at Insider blocks are opened or not
3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA
jobs”, filter jobs by Location - Istanbul, Turkey and department - Quality
Assurance, check presence of jobs list
4. Check that all jobs’ Position contains “Quality Assurance”, Department
contains “Quality Assurance”, Location contains “Istanbul, Turkey”
5. Click “View Role” button and check that this action redirects us to Lever

Application form page Test case should be written using any programming language and framework (Python or Java + Selenium would be preferable)
No BDD(Cucumber, Quantum, Codeception, etc.) frameworks are allowed Screenshot should be taken If test fails one of steps
Test case should be able to run in Chrome and Firefox browsers and ensure that the browser is parametrically changeable.
Test code should fully meet POM requirements
``` 


You can find my suggestion in [tests/task03.md](tests/task03/tests/test_insider_careers.py) written in Python using pytests.
To run locally you need to do the following:

1. Install dependencies:

``` python
pip install pytest selenium webdriver-manager
``` 
2. To run the tests:

``` python
pytest test_insider_homepage.py
``` 


# Task 4 
You can find my suggestion in [tests/task04.py](tests.task04.py) written in Python using pytests.
To run locally you need to do the following:

1. Configure Python environment
2. Install dependencies:

``` python
pip install pytest requests
``` 
3. Run tests:
> Test API. Using “pet” endpoints from https://petstore.swagger.io/ write CRUD operations API tests with positive and negative scenarios.

``` python
pytest test_petstore_api.py
``` 
