"""
    - Centralizes DB Connectivity
    - Gives a request-scoped session for the API
    - Uses configuration from config.py

    "How does the app safely talk to the DB"
"""
from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


