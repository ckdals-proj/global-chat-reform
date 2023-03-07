from .base import Base
from sqlalchemy import Column, String, Boolean, Integer
from .mixin import Timestamp

from .mixin import Timestamp

class User(Base, Timestamp):
    username = Column(String(20),unique=True)
    hashpw = Column(String(40))
    profile_pic = Column(String(100))
    is_active = Column(Boolean,default=True)
    lang = Column(String(10))
    friend_count = Column(Integer,default=0)