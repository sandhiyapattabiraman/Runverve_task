from pydantic import BaseModel


class UserDeviceCreate(BaseModel):
    device_id: str
    deviceName: str
    