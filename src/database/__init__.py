from core.config import DATABASE_URI, DATABASE_NAME
from .manager import DBManager

manager = DBManager(DATABASE_URI, DATABASE_NAME)
client = manager.get_client()
db = manager.get_db()
