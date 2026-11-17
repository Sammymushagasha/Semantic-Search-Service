from collections.abc import Generator

from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


# Creates the reusable connection setup for PostgreSQL.
engine: Engine = create_engine(
    settings.database.database_url,
    pool_pre_ping=True,
)

# Makes a separate database session available for each request.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db() -> Generator[Session, None, None]:
    """Provides one database session and closes it when the request ends."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
