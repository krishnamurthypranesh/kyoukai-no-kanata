from datetime import datetime

from sqlalchemy import Boolean, CHAR, Column, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class RequestReceived(Base):
    __tablename__ = "requests_received"

    id = Column(Integer, primary_key=True, index=True)
    gid = Column(CHAR(50), unique=True, index=True)
    request = Column(JSON, nullable=False, comment="request body with headers")
    response = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))
