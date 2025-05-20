from fastapi import APIRouter, Depends
from .user_matrix_schema import Matrix
from ..utils.database import Session
from .user_matrix_service import MatrixService
from ..utils.auth import authenticate
from uuid import UUID




matrix_router = APIRouter(prefix="/userMatrix", tags=["User Matrix"])

@matrix_router.post("/")
def add_user_matrix(details: Matrix, current_user: UUID = Depends(authenticate)):
    result = MatrixService.add_matrix( current_user, details)
    return {"success": True,"data": result}

@matrix_router.get("/")
def get_user_matrix(current_user: UUID = Depends(authenticate)):
    result = MatrixService.get_all_matrix( current_user)
    return {"success": True, "data": result}


