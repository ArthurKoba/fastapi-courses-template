from pymongo import MongoClient
from pymongo.database import Database


class DBManager:
    def __init__(self, host: str, db_name: str):
        self.__client = MongoClient(host)
        self.__db = self.__client[db_name]

    def show_databases(self):
        for db in self.__client.list_databases():
            print(db)

    def get_client(self) -> MongoClient:
        return self.__client

    def get_db(self) -> Database:
        return self.__db

    def close(self):
        self.__client.close()
