from fastapi import APIRouter, Depends
from typing import Optional

from dependency_injector.wiring import inject, Provide

from app.container import Container

from app.schemas.module import *


router = APIRouter(
    prefix="/login",
    tags=['login'],
    responses={404: {"description": "Not found"},'403':{"description":"Not Authentication"}},
)

@router.post('/')
@inject
async def login_with_access_toke(
    form_data: Login,
    category_service:CategoryService = Depends(Provide[Container.category_service])):

    if not name:
        return category_service.read_all_name()
    else: 
        return category_service.read_name(name)


@app.post('/api/v1/login', response_model=Token)
async def login_with_access_token(
    form_data: Login,db=Depends(get_db)):
    user:Union[User,None] = authenticate_user(username = form_data.username, password = form_data.password, db=db)
    if not user:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = 'Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
            )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub' : user.username, 'user_id' : user.id},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}