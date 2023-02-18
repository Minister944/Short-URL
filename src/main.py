from fastapi import FastAPI, Request
from src import schemas
from src.database import models
import os
from dotenv import load_dotenv
from src.database.db_conf import get_db
import random
from fastapi.responses import RedirectResponse

app = FastAPI()
load_dotenv()


@app.get("/{short_key}")
def redirect_url(short_key: str, request: Request):
    with get_db() as db:
        db_url = (
            db.query(models.URL)
            .filter(models.URL.short_key == short_key, models.URL.is_active)
            .first()
        )

    if db_url:
        return RedirectResponse(db_url.original_url)


@app.post("/short-url")
def create_url(url: schemas.URL):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    short_key = "".join(random.choice(chars) for _ in range(8))
    new_url = models.URL(short_key=short_key, original_url=url.url)
    with get_db() as db:
        db.add(new_url)
        db.commit()
    return schemas.URL(url=short_key)
