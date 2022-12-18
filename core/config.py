from starlette.config import Config

config = Config(".env")

SUPERUSER_TOKEN = config("SUPERUSER_TOKEN", cast=str, default="123456")

DATABASE_URI = config("DATABASE_URI", cast=str, default="mongodb://127.0.0.1:27017")
DATABASE_NAME = config("DATABASE_NAME", cast=str, default="courses")




