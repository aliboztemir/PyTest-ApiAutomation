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

#### [PROBLEM] Problems seen in question 1.
*In option b, the question asked to compare the total weight value with the carrying_capacity value. But some items did not have a weight value. I added condition in case of null.
*Test steps c and d failed. The values in the test outputs did not pass the assert rule.

![Test Report Screenshot](https://github.com/aliboztemir/PyTest-ApiAutomation/blob/main/screenshot/Test%20Report.png)

##  Question 2:

* I will share the details of the answer to this question via e-mail

#### [PROBLEM] Problems seen in question 2.

* In general, there were some shortcomings in the business rules. That's why I didn't ask you questions again. I have defined some conditions as I understand them. I designed test scenarios accordingly.

* is there Origination point input? Is the current location of the trucker owner being sent to the api? Does Origination take into account when calculating API routes?

* Are fuel station, grocery and bank different entities/input type?

* What is the input(address list) type? (json array, comma separated text, file etc)

* Will we always accept the place list added by the truck owner as correct?


##  Question 3:

* For the third question, you can see the test cases written in gherkin language under the ../features folder
