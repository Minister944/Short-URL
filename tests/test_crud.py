import pytest

from src.crud import create_url_db, get_by_short_key
from src.database.db_conf import get_db


def test_create_url_and_get(reset_db):
    short_key = "TJHDSDS"
    original_url = "https://example.com/"
    with get_db() as db:
        create_url_db(db, short_key, original_url)
        url = get_by_short_key(db, short_key)
        assert url.original_url == original_url
        assert url.short_key == short_key


def test_create_url_and_get_empty_original_key(reset_db):
    short_key = "TJHDSDS"
    original_url = ""
    with get_db() as db:
        create_url_db(db, short_key, original_url)
        url = get_by_short_key(db, short_key)
        assert url.original_url == original_url
        assert url.short_key == short_key
