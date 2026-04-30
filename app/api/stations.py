from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.station import StationResponse, StationCreate
from app.models.station import Station
from app.schemas.station import StationResponse


# Initialize the router for this file
router = APIRouter()


@router.post("/stations", response_model=StationResponse, status_code=201)
def create_station(station: StationCreate, db: Session = Depends(get_db)):
    # Create a new station instance based on the incoming data
    new_station = Station(
        name = station.name,
        location = station .location,
        is_online = station.is_online,
    )


    # Add the new station to the database session and commit it
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return new_station





@router.get("/stations/{station_id}", response_model=StationResponse)
def get_station(station_id: int, db: Session = Depends(get_db)):
    # retrieving a specific station from the database based on the provided station id
    station = db.query(Station).filter(Station.id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station