import bcrypt
from .user_model import User, UserDao
from ..utils.auth import jwt_token_encrypt
from ..utils.database import Session, engine
from sqlmodel import  select



class UserService():
    def hash_password(password: str) -> str:
     salt = bcrypt.gensalt()
     hashed_password = bcrypt.hashpw(password.encode(), salt)
     return hashed_password.decode()
    
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    
    def create_user(user_create):
        hashed_password = UserService.hash_password(user_create.password)  
        new_user=User(   
        email=user_create.email,
        password=hashed_password
        )
        
        new_users=UserDao.create_user(new_user)
        token=jwt_token_encrypt(new_users)
        return {"email":new_user.email,"token":token}
    
    def authenticate_user(user_login):
        user = UserDao.get_user_byemail(user_login.email)
        
        if not user:
            return None 

        if not UserService.verify_password(user_login.password, user.password):
            return None  

        token = jwt_token_encrypt(user)
        print(token)
        return {"access_token": token, "token_type": "bearer"}
    
    def get_user(user_id):
        with Session(engine) as session:
            user = session.exec(select(User).where(User.id == user_id)).first()
            return user
