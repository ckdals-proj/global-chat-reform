from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from contextlib import contextmanager, AbstractContextManager

from typing import Callable

import os

class DataBase:
    def __init__(self, db_url:str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = scoped_session(
            sessionmaker(bind=self._engine,autoflush=False)
        )

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()

        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    

