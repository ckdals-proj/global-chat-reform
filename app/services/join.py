from typing import Union, Optional
from fastapi import HTTPException, status

from app.models.module import User
from app.core.auth import pwd_context
from app.repositories.module import UserRepository
from datetime import timedelta, utcnow

from jose import jwt

from app.core.const import ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi import UploadFile
from starlette.responses import RedirectResponse
import os


class JoinService:
    def __init__(self, user_repository:UserRepository) -> None:
        self.user_repository = user_repository

    def join(self,file:UploadFile, lang:str, password:str, username:str):
        select_lang = 'ko' if lang == 'ko' else 'en'
        hashpw = pwd_context.hash(password)
        user = User(username=username,hashpw=hashpw,lang=select_lang,profile_pic='/static/pictures/'+username+'/profile.jpg')

        content = file.file.read()
        file.file.close()

        try:
            self.user_repository.save(user=user,username=username,content=content)
            path = './static/pictures/'+username
            if not os.path.isdir(path):
                os.mkdir(path)
            with open(path+'/profile.jpg',mode='wb') as f:
                f.write(content)
        
            return RedirectResponse(url='/join/success',status_code=302)

        except Exception as e:
            print(e)
            return RedirectResponse(url='/join/fail',status_code=302)
