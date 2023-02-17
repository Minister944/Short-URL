from fastapi import FastAPI
from src import schemas
from src.database import models
import os
from dotenv import load_dotenv
from src.database.db_conf import get_db

app = FastAPI()
load_dotenv()


@app.get("/")
def start_page():
    print(os.environ["DB_URL"])
    return "Main page"


@app.post("/short-url")
def create_url(url: schemas.URLSchema):
    new_url = models.URL(short_key="test", original_url=str(url), is_active=True)
    with get_db() as db:
        db.add(new_url)
        db.commit()
    return url
