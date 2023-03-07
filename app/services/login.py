from typing import Union, Optional
from fastapi import HTTPException, status

from app.models.module import User
from app.core.auth import pwd_context
from app.repositories.module import UserRepository
from datetime import timedelta, utcnow

from jose import jwt

from app.core.const import ACCESS_TOKEN_EXPIRE_MINUTES

import os


class LoginService:
    def __init__(self, user_repository:UserRepository) -> None:
        self.user_repository = user_repository

    def verify_password(self, input_password, db_password):
        return pwd_context.verify(input_password, db_password)
        # return input_password == db_password

    def authenticate_user(self, username: str, password: str, user_repository:UserRepository):
        userinfo:Union[User,None] = user_repository.find(username)

        if not userinfo:
            return False

        db_password = userinfo.hashpw
        if not self.verify_password(password, db_password):
            return False
        return userinfo
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = utcnow() + expires_delta
        else:
            expire = utcnow()
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, os.environ.get("SECRET_KEY"), algorithm=os.environ.get("ALGORITHM"))
        return encoded_jwt
    
    def login(self,form_data):
        user:Union[User,None] = self.authenticate_user(
            username = form_data.username, 
            password = form_data.password, user_repository=self.user_repository)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail = 'Incorrect username or password',
                headers={'WWW-Authenticate': 'Bearer'}
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={'sub' : self.user.username, 'user_id' : self.user.id},
            expires_delta=access_token_expires
        )
        return {'access_token': access_token, 'token_type': 'Bearer'}