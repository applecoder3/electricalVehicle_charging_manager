from pydantic import BaseModel, ConfigDict 
from typing import Optional
from datetime import datetime



class SessionBase(BaseModel):

    start_battery_level: int


class SessionCreate(SessionBase):
    pass


class SessionEnd(BaseModel):
    end_battery_level: int

class SessionResponse(SessionBase):
    
    id: int
    station_id: int
    end_battery_level: Optional[int] = None
    start_time: datetime
    end_time: Optional[datetime] = None

    """variable Must be the same variable as what located in the session model"""
    charge_duration: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
