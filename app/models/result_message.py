from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class ResultMessage(Base):
    origin_id = Column(Integer,ForeignKey('origin_message.id'))
    body = Column(String(100))
    lang = Column(String(10))

    message_historys = relationship("MessageHistory",back_populates="result_message",uselist=False)
    origin_messages = relationship("OriginMessage",foreign_keys=[origin_id],back_populates="result_message")