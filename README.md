# Semantic-Search-Service

Backend for meaning-based semantic and hybrid search. The planned system includes document ingestion, vector indexing, reranking, and search evaluation.

## Current implementation

The API currently has health and root routes, a PostgreSQL SQLAlchemy engine and request-scoped sessions in `app/db/session.py`, and document/chunk models in `app/db/models.py`. Chunks include a pgvector embedding field sized from `EMBEDDING_DIM` (384 by default). PostgreSQL's `vector` extension must be enabled before these tables are created. PostgreSQL connections use the psycopg 3 driver. The engine connects lazily when a database operation first uses a session; the health and root routes do not require a database connection. Database migrations and automatic table creation are not set up yet.

## Run locally

From the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

By default, the app uses `postgresql+psycopg://localhost:5432/semantic_search`. Set `DATABASE_URL` in the environment to use your PostgreSQL credentials or a different host. Create the database before adding endpoints that query it. API docs are available at `/docs`.
