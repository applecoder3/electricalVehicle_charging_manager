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

    model_config = ConfigDict(from_attributes=True)
