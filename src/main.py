from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from src import schemas
from src.database.db_conf import get_db
from src.generator import random_str
from src.crud import get_by_short_key, create_url_db


app = FastAPI()


@app.get("/{short_key}")
def redirect_url(short_key: str, request: Request):
    with get_db() as db:
        if url := get_by_short_key(db, short_key):
            return RedirectResponse(url.original_url)

    return HTMLResponse(status_code=404, content="Not Found URL")


@app.post("/short-url")
def create_url(url: schemas.URL):
    short_key = random_str()
    with get_db() as db:
        create_url_db(db, short_key=short_key, original_url=url.url)

    return schemas.URL(url=short_key)
