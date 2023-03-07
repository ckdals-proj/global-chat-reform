from dependency_injector import containers, providers

from app.db.database import DataBase

from app.services.module import *
from app.repositories.module import UserRepositor

from app.repositories.module import *

import os


class Container(containers.DeclarativeContainer):
    #database
    db = providers.Singleton(DataBase,db_url=os.environ.get('DB_SESSION'))
    
    #repositories
    user_repository = providers.Factory(UserRepositor, session_factory=db)
    
    #services
    login_serivce = providers.Factory(LoginService,user_repository=user_repository)
    join_service = providers.Factory(JoinService,user_repository=user_repository)
