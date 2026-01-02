from typing import Optional
from pydantic import BaseModel
import os


# ------------
# Environment
# ------------

class AppConfig(BaseModel):
    """Core application settings."""
    app_name: str = "Semantic Search Service"
    environment: str = os.getenv("APP_ENV", "development")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"


# -------
# Server
# -------

class ServerConfig(BaseModel):
    """API server configuration."""
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", 8000))


# ---------
# Database
# ---------

class DatabaseConfig(BaseModel):
    """Database connection settings."""
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/semantic_search"
    )


# -------------------
# Search & Retrieval
# -------------------

class SearchConfig(BaseModel):
    """Search and retrieval configuration."""
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    embedding_dimension: int = int(os.getenv("EMBEDDING_DIM", 384))

    chunk_size: int = int(os.getenv("CHUNK_SIZE", 500))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", 50))

    default_top_k: int = int(os.getenv("DEFAULT_TOP_K", 10))
    hybrid_alpha: float = float(os.getenv("HYBRID_ALPHA", 0.5))


# --------------
# Feature Flags
# --------------

class FeatureFlags(BaseModel):
    """Feature toggles for experimentation."""
    enable_hybrid_search: bool = os.getenv("ENABLE_HYBRID_SEARCH", "true").lower() == "true"
    enable_reranking: bool = os.getenv("ENABLE_RERANKING", "false").lower() == "true"
    enable_caching: bool = os.getenv("ENABLE_CACHING", "false").lower() == "true"


# -------------------
# Aggregate Settings
# -------------------

class Settings(BaseModel):
    app: AppConfig = AppConfig()
    server: ServerConfig = ServerConfig()
    database: DatabaseConfig = DatabaseConfig()
    search: SearchConfig = SearchConfig()
    features: FeatureFlags = FeatureFlags()


# Global settings instance
settings = Settings()
