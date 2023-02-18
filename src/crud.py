from src.database.db_conf import get_db
from src.database import models


def get_by_short_key(db, short_key: str) -> models.URL:
    with get_db() as db:
        url: models.URL = (
            db.query(models.URL)
            .filter(models.URL.short_key == short_key, models.URL.is_active)
            .first()
        )
    return url


def create_url_db(db, short_key: str, original_url: str):
    new_url = models.URL(short_key=short_key, original_url=original_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
