from fastapi import APIRouter, Depends
from uuid import UUID
from ..utils.auth import authenticate
from .product_service import UserDeviceService
from .product_schema import UserDeviceCreate


device_router = APIRouter(prefix="/devices", tags=["devices"])

@device_router.post("/")
def create_device(
    device_data: UserDeviceCreate,
    current_user: UUID = Depends(authenticate),
):
    device = UserDeviceService.add_device( current_user, device_data)
    return device