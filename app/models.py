from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class QueryHistory(Base):
    """Модель для хранения кадастровых записей."""
    __tablename__ = "query_history"

    id = Column(Integer, primary_key=True, index=True)
    cadastral_number = Column(String, index=True, unique=True)
    latitude = Column(Float)
    longitude = Column(Float)
    result = Column(Boolean)
