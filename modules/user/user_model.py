from sqlmodel import SQLModel, Field, select
from uuid import uuid4, UUID
from pydantic import EmailStr
from ..utils.database import Session, engine




class User(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    email: EmailStr = Field(unique=True)
    password: str

class UserDao:
    def create_user(new_user):
        with Session(engine) as session:
         session.add(new_user)
         session.commit()
         session.refresh(new_user)
        return new_user
    
    def get_user_byemail(email):
     with Session(engine) as session:
         users=session.exec(select(User).where(User.email==email)).first()
         return users

