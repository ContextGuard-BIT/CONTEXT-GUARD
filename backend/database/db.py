"""
Database models and session management.
Uses SQLAlchemy with SQLite by default (easy local dev).
Switch DATABASE_URL in .env to PostgreSQL for production.
"""
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from backend.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class AnalysisRecord(Base):
    """Stores every analysis result for history / audit."""
    __tablename__ = "analysis_records"

    id           = Column(Integer, primary_key=True, index=True)
    created_at   = Column(DateTime, default=datetime.utcnow)
    claim        = Column(Text,    nullable=False)
    source       = Column(Text,    nullable=False)
    score        = Column(Integer, nullable=False)
    category     = Column(String(64), nullable=False)
    confidence   = Column(Float,   nullable=False)
    nli_label    = Column(String(32))
    similarity   = Column(Float)
    explanation  = Column(Text)


def create_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    """FastAPI dependency: yields a DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
