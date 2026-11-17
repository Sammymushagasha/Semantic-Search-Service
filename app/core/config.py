import os
from pydantic import BaseModel


# Holds basic app settings, with optional environment overrides.
class AppConfig(BaseModel):
    """Basic app settings."""
    # Names the app and selects its run mode.
    app_name: str = "Semantic Search Service"
    environment: str = os.getenv("APP_ENV", "development")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"


# Holds the address and port for the API server.
class ServerConfig(BaseModel):
    """API server settings."""
    # Sets where the server listens.
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", 8000))


# Holds the address used to connect to PostgreSQL.
class DatabaseConfig(BaseModel):
    """Database settings."""
    # Uses the supplied address or a local default.
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://localhost:5432/semantic_search"
    )


# Holds the settings used later by search and document chunking.
class SearchConfig(BaseModel):
    """Search settings."""
    # Chooses the model and size used for text embeddings.
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    embedding_dimension: int = int(os.getenv("EMBEDDING_DIM", 384))

    # Sets chunk length and how much neighboring chunks overlap.
    chunk_size: int = int(os.getenv("CHUNK_SIZE", 500))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", 50))

    # Sets the result count and semantic-versus-keyword balance.
    default_top_k: int = int(os.getenv("DEFAULT_TOP_K", 10))
    hybrid_alpha: float = float(os.getenv("HYBRID_ALPHA", 0.5))


# Holds switches for optional search features.
class FeatureFlags(BaseModel):
    """Optional feature switches."""
    # Turns hybrid search, reranking, or caching on and off.
    enable_hybrid_search: bool = os.getenv("ENABLE_HYBRID_SEARCH", "true").lower() == "true"
    enable_reranking: bool = os.getenv("ENABLE_RERANKING", "false").lower() == "true"
    enable_caching: bool = os.getenv("ENABLE_CACHING", "false").lower() == "true"


# Groups all app settings in one place.
class Settings(BaseModel):
    app: AppConfig = AppConfig()
    server: ServerConfig = ServerConfig()
    database: DatabaseConfig = DatabaseConfig()
    search: SearchConfig = SearchConfig()
    features: FeatureFlags = FeatureFlags()


# Makes the settings available throughout the app.
settings = Settings()
