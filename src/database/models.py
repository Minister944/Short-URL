from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class URL(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    short_key = Column(String)
    original_url = Column(String)
    is_active = Column(Boolean)