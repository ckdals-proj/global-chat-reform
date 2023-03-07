from .base import Base
from sqlalchemy import Column, Boolean, Integer, ForeignKey,DateTime
from sqlalchemy.orm import relationship

from .mixin import Timestamp

class MessageHistory(Base,Timestamp):
    room_id = Column(Integer,ForeignKey('room.id'))
    from_id = Column(Integer)
    to_id = Column(Integer)
    origin_id = Column(Integer,ForeignKey('origin_message.id'))
    result_id = Column(Integer,ForeignKey('result_message.id'))

    origin_messages = relationship("OriginMessage",foreign_keys=[origin_id],back_populates="message_history")
    result_messages = relationship("ResultMessage",foreign_keys=[result_id],back_populates="message_history")