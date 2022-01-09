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
