from .base import Base
from sqlalchemy import Column, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .mixin import Timestamp

class Friend(Base, Timestamp):
    user_id = Column(Integer,ForeignKey('user.id'))
    friend_id = Column(Integer,ForeignKey('user.id'))
    state = Column(Integer,default=0) # 요청대기: 0, 요청미응답: 1, 요청완료: 2
    room_id = Column(Integer,ForeignKey('room.id'))

    users = relationship("User",foreign_keys=[user_id])
    friends = relationship("User",foreign_keys=[friend_id])
    # rooms = relationship("Room",foreign_keys=[room_id])