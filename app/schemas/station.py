from pydantic import BaseModel, ConfigDict 
from typing import Optional, List

from app.schemas.session import SessionResponse

class StationBase(BaseModel):
    name: str
    location: str
    is_online: bool

class StationCreate(StationBase):
    pass

class StationUpdate(StationBase):
    name: Optional[str] = None
    location: Optional[str] = None
    is_online: Optional[bool] = None
    current_status: Optional[str] = None

class StationDelete(BaseModel): 
    id: int

class StationResponse(StationBase):
    id: int
    current_status: str # e.g "available", "occupied", "offline"

    sessions: List[SessionResponse]= []

    model_config = ConfigDict(from_attributes=True)

