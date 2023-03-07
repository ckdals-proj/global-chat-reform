from .base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .mixin import Timestamp

class Room(Base, Timestamp):
    friends = relationship("Friend")
    message_historys = relationship("MessageHistory")