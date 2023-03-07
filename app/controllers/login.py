from fastapi import APIRouter, Depends
from typing import Optional

from dependency_injector.wiring import inject, Provide

from app.container import Container

from app.schemas.module import *

from app.services.module import LoginService


router = APIRouter(
    prefix="/login",
    tags=['login'],
    responses={404: {"description": "Not found"},'403':{"description":"Not Authentication"}},
)

@router.post('/',response_model=Token)
@inject
async def login_with_access_toke(
    form_data: Login,
    login_service:LoginService = Depends(Provide[Container.login_service])):

    login_service.login(form_data=form_data)
