from sqlmodel import SQLModel, Field, select
from uuid import uuid4, UUID
from pydantic import EmailStr
from ..utils.database import Session, engine
from ..user.user_model import User
from datetime import datetime
from ..product.product_model import UserDevice



class UserMatrix(SQLModel, table = True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    userId: UUID = Field(foreign_key="user.id")
    deviceId: str = Field(foreign_key="userdevice.device_id")
    hydration: float
    fatigue: str
    posture: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)   
    


class MatrixDao:
    
    def add_matrix(current_user, matrix_data):
        with Session(engine) as session:
            device = session.exec(
                select(UserDevice).where(
                    (UserDevice.device_id == matrix_data.deviceId) &
                    (UserDevice.userId == current_user)
                )
            ).first()

            if not device:
                raise Exception("Invalid device ID or device does not belong to the user.")

            matrix = UserMatrix(
                userId=current_user,
                deviceId=matrix_data.deviceId,
                hydration=matrix_data.hydration,
                fatigue=matrix_data.fatigue,
                posture=matrix_data.posture
            )
            session.add(matrix)
            session.commit()
            session.refresh(matrix)
            return matrix

    def get_all_matrix( current_user):
        with Session(engine) as session:
            return session.exec(select(UserMatrix).where(UserMatrix.userId == current_user)).all()