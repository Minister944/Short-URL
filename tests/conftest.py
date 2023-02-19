import os

import pytest
from sqlalchemy import create_engine

from src.database.db_conf import get_db
from src.database.models import URL, Base


@pytest.fixture(scope="session", autouse=True)
def fake_db():
    engine = create_engine(os.environ["DB_URL"])
    Base.metadata.create_all(engine)


@pytest.fixture
def reset_db():
    with get_db() as db:
        db.query(URL).delete()
        db.commit()
