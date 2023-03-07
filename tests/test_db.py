from app.main import app
from app.db.database import Session, DataBase

from app.container import Container

def test_scoped_session():
    session = Container.db.provided.session

    a_session = session()

    b_session = session()

    assert a_session == b_session, "두개의 객체가 서로 다르다."