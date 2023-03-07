from sqlalchemy import Column, DateTime, Boolean
from app.utils.timestamp import service_time

class Timestamp:
    created_at = Column(DateTime,default=service_time)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_deleted = Column(Boolean,default=False)
    