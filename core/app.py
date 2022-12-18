from fastapi import FastAPI
from pymongo.database import Database

from database import db, client


class Application(FastAPI):
    db: Database


app = Application()


@app.on_event("startup")
def start_app():
    app.db = db


@app.on_event("shutdown")
def stop_app():
    client.close()

