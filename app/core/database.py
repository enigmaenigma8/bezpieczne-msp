"""
Konfiguracja połączenia z bazą danych.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://bezpieczne:bezpieczne@localhost:5432/bezpieczne_msp"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Tworzy tabele w bazie (jeśli nie istnieją)."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency do FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
