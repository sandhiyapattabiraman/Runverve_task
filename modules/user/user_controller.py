from fastapi import APIRouter, HTTPException, Depends
from .user_service import UserService
from .user_schema import UserCreate, UserLogin
from uuid import UUID
from ..utils.auth import authenticate



user_router = APIRouter(prefix="/user" , tags=["User"])


@user_router.post("/signin")
def create_user(user:UserCreate):
    return UserService.create_user(user)

@user_router.post("/login")
def login_user(user_login:UserLogin):
    user= UserService.authenticate_user(user_login)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = user.get('access_token')
    if not access_token:
        raise HTTPException(status_code=500, detail="Error generating access token")

    return {"access_token": user["access_token"], "token_type": "bearer"}


@user_router.get("/current-user")
def current_user(current_user: UUID = Depends(authenticate)):
    user = UserService.get_user(current_user)
    return {'username': user.email}