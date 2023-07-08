from datetime import datetime

from sqlalchemy import Boolean, Char, Column, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class RequestReceived(Base):
    id = Column(Integer, primary_key=True, index=True)
    gid = Column(Char(50), unique=True, index=True)
    request = Column(Text, null=False)
    response = Column(Text, null=False)
    created_at = Column(DateTime(timezone=True), default_func=datetime.now)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now)
