from fastapi import FastAPI, HTTPException
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/deliveries", status_code=200)
def read_user():
    return api.deliveries_for_planning()


@app.get("/route", status_code=200)
def read_user():
    return api.planned_routes()