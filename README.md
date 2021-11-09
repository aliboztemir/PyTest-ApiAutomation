# QA Test Engineer: Assignment
Tests of the API that calculates the best route.

## Preconditions:

- Python 3

## Clone the project

```
git clone https://github.com/aliboztemir/PyTest-ApiAutomation
```

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest test/test.py --html=report.html --self-contained-html
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

##  Project Structure
* Programming Language: Python 3
* IDE: PyCharm
* OS : macOs x
* mock APIs were created with fastapi

##  Question 1:

* The get operations of mock APIs are done in ../app/api/main.py
* The test outputs are in the ../data folder
* For the 1st question, 5 test scripts were developed using pytest ../test/test.py
* The pytest-html plugin was used to report the test results. You can view the report.html file under the main folder from the browser.
* 3 of the test scenarios passed and 2 of them failed.
* If you want, you can run the tests in your local or with docker
* Not: If you want to run the tests individually from the ide in your local, you should update the relative path in api.py. Paths are configured to run in terminal. For example: '../data/deliveries_for_planning.json'

![Test Report Screenshot](https://github.com/aliboztemir/PyTest-ApiAutomation/blob/main/screenshot/Test%20Report.png)


### [PROBLEM] During the tests, the following problems were seen.

* Minimum length check can be added for "api/v1/tasks" api.

* Bad character check can be added for "api/v1/tasks" api. For example: "'+&/)&++"

* For PutTaskAPI, when we send a "null" value to the title field, it should give an error, but it acts as if it is updating.

* Min length and bad character control can be added for PutTaskAPI.

* There is a general problem for all api's. If we set the endpoints as invalid and call them, the .php extension files are displayed for the error message. A safer and more understandable error message may be displayed. Displaying all php file paths can also cause a security vulnerability.

* Likewise, when the "id" field is sent invalid at the endpoints of getTaskAPI, putTaskAPI and getTaskAPI, the response message appears to be problematic. Again, the line numbers of the code file with the .php extension error are displayed. The error level must be changed.
