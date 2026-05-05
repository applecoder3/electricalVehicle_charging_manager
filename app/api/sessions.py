from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.session import SessionCreate, SessionResponse, SessionEnd

from app.models.session import Session as SessionModel
from app.models.station import Station as StationModel
from app.db.database import get_db

from datetime import datetime, timezone

router = APIRouter()


@router.post("/stations/{station_id}/sessions", response_model=SessionResponse)
def start_charging_session(station_id: int, session_data: SessionCreate, db: Session = Depends(get_db)):
    station = db.query(StationModel).filter(StationModel.id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    if not station.is_online:
        raise HTTPException(status_code=400, detail="Station is offline")
    
    station.current_status = "Occupied"

    new_session = SessionModel(
        station_id = station_id,
        start_battery_level = session_data.start_battery_level
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return new_session


@router.patch("/stations/{station_id}/sessions", response_model=SessionResponse)
def end_charging_session(session_id: int, session_data: SessionEnd, db:Session = Depends(get_db)):
    
    '''Ending an active charging session which will free up the station'''

    #Find the session
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    #Preventing ending a sesison that is already ended
    if session.end_time is not None:
        raise HTTPException(status_code=400, detail="This session has already ended.")
    
    
    #Update the Session record 
    session.end_time = datetime.now(timezone.utc)
    session.ending_battery_percentage = session_data.ending_battery_percentage

    #Checking to make sure battery is valid (the ending battery percentage is not lower than when it started and the ending battery percentage does not exceed 100 percent)
    if session_data.ending_battery_percentage < session.start_battery_level:
        raise HTTPException(status_code=400, detail="Ending battery cannot be lower than starting battery.")
    if session_data.ending_battery_percentage > 100:
        raise HTTPException(status_code=400, detail="Battery percentage cannot exceed 100.")

    # Find the parent station and update its status back to available
    station = db.query(StationModel).filter(StationModel.id == session.station_id).first()
    if station:
        station.current_status = "Available"

    db.commit()
    db.refresh(session)
    return session