from pydantic import BaseModel
from datetime import datetime

class VehicleCreate(BaseModel):
    plate: str

class VehicleUpdate(BaseModel):
    exit_time: datetime | None = None
    payment_amount: float | None = None
    is_paid: bool | None = None

class Vehicle(BaseModel):
    id: int
    plate: str
    entry_time: datetime
    exit_time: datetime | None
    payment_amount: float | None
    is_paid: bool

    class Config:
        from_attributes = True  # Para compatibilidade com SQLAlchemy
