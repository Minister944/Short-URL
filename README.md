# Short-URL

This is a simple application to shorten links.

### Used technologies:

- Docker
- SQLAlchemy
- FastAPI
- Alembic
- Poetry
- PostgreSQL

### Endpoint

![endpoint](img/api.png)

### Example .env

```
DB_URL=postgresql+psycopg2://postgres:postgres@db:5432/test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=test_db
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=qwerty
```

# How to Run

### Docker:

```bash
docker-compose build
docker-compose up
```

### Local:

You must run the database local.

```bash
alembic upgrade head
poetry lock
poetry install
uvicorn src.main:app --reload
```
