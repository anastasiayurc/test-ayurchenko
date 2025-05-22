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


You can find my suggestion in [tests/task03/task03.md](tests/task03/tests/test_insider_careers.py) written in Python using pytests.
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
You can find my suggestion in [tests/task04/task04.py](tests/task04/task04.py) written in Python using pytests.
To run locally you need to do the following:

1. Configure Python environment
2. Install dependencies:

``` python
pip install pytest requests
``` 
3. Run tests:
> Test API. Using “pet” endpoints from https://petstore.swagger.io/ write CRUD operations API tests with positive and negative scenarios.

``` python
pytest tests/task04.py
```

Another way to create API tests using such tools as [Postman](https://learning.postman.com/), [Postman tests](https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/) and [Newman](https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman/) for running the tests either locally or in the CI/CD pipeline

Example of running Postman Collection in the terminal:a
```
macintosh@Macintoshs-Laptop Desktop % newman run Pet.postman_collection.json              
newman

Pet

→ pet/{petId} Find pet by ID Positive
  GET https://petstore.swagger.io/v2/pet/9223372036854758000 [200 OK, 482B, 636ms]

→ pet/{petId} Find pet by ID Negative
  GET https://petstore.swagger.io/v2/pet/9223372036854758000 [404 Not Found, 384B, 141ms]
  ✓  Response status code is not 200
  1. Verify that the response contains an error message or code
  2. Invalid input handling for non-existent petId
  ✓  Verify response for negative or non-integer petId
  3. Proper error handling and error message format

→ pet Add a new pet to the store Positive
  POST https://petstore.swagger.io/v2/pet [200 OK, 482B, 141ms]
  ✓  Save pet ID into a collection variable
  ✓  Response status code is 200
  ✓  Response time is in an acceptable range
  ✓  Validate the response schema for the required fields
  ✓  Category object contains the required fields - id and name
  ✓  Status field should be a non-empty string

→ pet Add a new pet to the store Negative
  POST https://petstore.swagger.io/v2/pet [500 Server Error, 400B, 140ms]
  ┌
  │ 'Pet ID is not found in the expected path. Check the response structure.'
  └
  ✓  Save pet ID into a collection variable
  4. Response status code is 200
  ✓  Response time is in an acceptable range
  5. Validate the response schema for the required fields
  6. Category object contains the required fields - id and name
  7. Status field should be a non-empty string

→ pet/{petId} uploadImage
  POST https://petstore.swagger.io/v2/pet/1111032036854758000/uploadImage [200 OK, 437B, 1003ms]
 ✓  Response status code is not 200
  1. Verify that the response contains an error message or code
  2. Invalid input handling for non-existent petId

→ pet Update an existing pet
  PUT https://petstore.swagger.io/v2/pet [404 Not Found, 494B, 137ms]
   ✓  Response status code is not 200
  1. Verify that the response contains an error message or code
  2. Invalid input handling for non-existent petId

→ pet/{petId} Delete a pet
  DELETE https://petstore.swagger.io/v2/pet [200 OK, 482B, 141mss]
    ✓  Response status code is not 200
    1. Verify that the response contains an error message or code
    2. Invalid input handling for non-existent petId

┌─────────────────────────┬─────────────────────┬─────────────────────┐
│                         │            executed │              failed │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│              iterations │                   1 │                   0 │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│                requests │                   7 │                   1 │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│            test-scripts │                  10 │                   0 │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│      prerequest-scripts │                   7 │                   0 │
├─────────────────────────┼─────────────────────┼─────────────────────┤
│              assertions │                  17 │                   7 │
├─────────────────────────┴─────────────────────┴─────────────────────┤
│ total run duration: 2.3s                                            │
├─────────────────────────────────────────────────────────────────────┤
│ total data received: 707B (approx)                                  │
├─────────────────────────────────────────────────────────────────────┤
│ average response time: 366ms [min: 137ms, max: 1003ms, s.d.: 337ms] │
└─────────────────────────────────────────────────────────────────────┘

``` 


