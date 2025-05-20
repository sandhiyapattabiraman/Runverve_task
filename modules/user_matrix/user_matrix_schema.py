from pydantic import BaseModel


class Matrix(BaseModel):
    deviceId: str
    hydration: float
    fatigue: str
    posture: str


