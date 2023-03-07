from typing import Union

from app.models.module import User


def authenticate_user(username: str, password: str, db):
    userinfo:Union[User,None] = get_userinfo(username,db)

    if not userinfo:
        return False

    db_password = userinfo.hashpw
    if not verify_password(password, db_password):
        return False
    return userinfo

class LoginService:
    def __init__(self) -> None:
        ...

    def authenticate_user(self, username: str, password: str, db):
        userinfo:Union[User,None] = get_userinfo(username,db)

        if not userinfo:
            return False

        db_password = userinfo.hashpw
        if not verify_password(password, db_password):
            return False
        return userinfo

    def get_userinfo(self, username: str,db): # username으로 조회할지, primary_key인 id로 조회할지...
        try:
            user_info:User = db.query(User).filter(User.username == username).first()
            return user_info
        
        except Exception as e:
            print('db에서 유저를 조회할 수 없습니다')
            print(e)
            return None


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