from .base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class OriginMessage(Base):
    body = Column(String(100))
    lang = Column(String(10))

    message_historys = relationship("MessageHistory",back_populates="origin_message",uselist=False)
    result_messages = relationship("ResultMessage",back_populates="origin_message",uselist=False)