from typing import Dict
from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from sqlalchemy import select

from .base import BaseRepository

from app.models.module import User

import os

class UserRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def find(self, username):
        with self.session_factory() as session:
            stmt = select(User).where(User.username==username)
            user_info = session.scalars(stmt).first()
            return user_info
            
        
    def save(self,user:User):
        with self.session_factory() as session:
            session.add(user)
            session.commit()