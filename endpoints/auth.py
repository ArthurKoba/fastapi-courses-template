from core.app import app
from core.config import SUPERUSER_TOKEN
from models import Auth


@app.post("/auth/check")
def check_token(auth: Auth):
    if auth.token == SUPERUSER_TOKEN:
        return {"status": True}
    return {"status": False}
