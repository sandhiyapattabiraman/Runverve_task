from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from ..utils.database import Session, engine


class UserDevice(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    device_id: str = Field(unique=True)
    userId: UUID = Field(foreign_key="user.id")
    deviceName: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)


class UserDeviceDao:

    def create_device( user_id, device_data):
        with Session(engine) as session:
            device = UserDevice(
                userId=user_id,
                device_id=device_data.device_id,
                deviceName=device_data.deviceName,
            )
            session.add(device)
            session.commit()
            session.refresh(device)
            return device
