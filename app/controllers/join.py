from fastapi import APIRouter, Depends
from fastapi import UploadFile,Form
from typing import Optional

from dependency_injector.wiring import inject, Provide

from app.container import Container

from app.schemas.module import *

from app.services.module import JoinService


router = APIRouter(
    prefix="/join",
    tags=['join'],
    responses={404: {"description": "Not found"},'403':{"description":"Not Authentication"}},
)

@router.post('/',response_model=Token)
@inject
async def join(
    file: UploadFile, username: str = Form(), password: str = Form(), lang:str=Form(), 
    join_service:JoinService = Depends(Provide[Container.join_service])):

    join_service.join(file,lang,password,username)
