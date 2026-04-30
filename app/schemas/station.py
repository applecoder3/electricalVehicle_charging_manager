from pydantic import BaseModel, ConfigDict 
from typing import Optional

class StationBase(BaseModel):
    name: str
    location: str
    is_online: bool

class StationCreate(StationBase):
    pass

class StationUpdate(BaseModel):
    pass

class StationResponse(StationBase):
    id: int
    current_status: str # e.g "available", "occupied", "offline"

    model_config = ConfigDict(from_attributes=True)

