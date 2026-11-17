# Semantic-Search-Service

Backend for meaning-based semantic and hybrid search. The planned system includes document ingestion, vector indexing, reranking, and search evaluation.

## Current implementation

The API currently has health and root routes, plus a PostgreSQL SQLAlchemy engine and a request-scoped session dependency in `app/db/session.py`. PostgreSQL connections use the psycopg 3 driver. The engine is created at startup, but connects lazily when a database operation first uses a session; the health and root routes do not require a database connection.

## Run locally

From the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

By default, the app uses `postgresql+psycopg://localhost:5432/semantic_search`. Set `DATABASE_URL` in the environment to use your PostgreSQL credentials or a different host. Create the database before adding endpoints that query it. API docs are available at `/docs`.
