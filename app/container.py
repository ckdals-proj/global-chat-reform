from dependency_injector import containers, providers

from app.db.database import DataBase

import os


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(DataBase,db_url=os.environ.get('DB_SESSION'))
