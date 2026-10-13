"""
Modele bazy danych (SQLAlchemy).
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    connections = relationship("EmailConnection", back_populates="user")
    alerts = relationship("Alert", back_populates="user")


class EmailConnection(Base):
    __tablename__ = "email_connections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    email_address = Column(String, nullable=False)
    provider = Column(String)  # np. "gmail", "imap"
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="connections")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sender = Column(String)
    subject = Column(String)
    risk_level = Column(String)  # niskie / średnie / wysokie
    risk_score = Column(Integer)
    reasons = Column(Text)  # JSON lub tekst
    recommendation = Column(Text)
    is_false_positive = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="alerts")
