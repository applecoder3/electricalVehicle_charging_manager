from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.station import StationResponse, StationCreate, StationUpdate
from app.models.station import Station
from app.schemas.station import StationResponse



# Initialize the router for this file
router = APIRouter()


@router.post("/", response_model=StationResponse, status_code=201)
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

@router.patch("/{station_id}", response_model = StationResponse, status_code=200)
def patch_station(station_id: int, station_patch: StationUpdate, db: Session = Depends(get_db)):
    # Retrive the staiton to be updated from the database
    station = db.query(Station).filter(Station.id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")

    # extract the fields to be updated from the incoming data and update the station's attributes
    update_data = station_patch.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(station, key, value)
    
    db.commit()
    db.refresh(station)
    return station

@router.put("/{station_id}", response_model=StationResponse, status_code=200)
def update_station(station_id: int, station_update: StationCreate, db: Session = Depends(get_db)):

    # Retrieve the station to be updated from the database
    station = db.query(Station).filter(Station.id == station_id).first()
    if not station: 
        raise HTTPException(status_code=404, detail="Station not found")
    
    # Update the station's attributes based on the incoming data
    station.name = station_update.name
    station.location = station_update.location
    station.is_online = station_update.is_online
    

    # Commit the changes to the database
    db.commit()
    db.refresh(station)
    return station


@router.get("/{station_id}", response_model=StationResponse)
def get_station(station_id: int, db: Session = Depends(get_db)):
    # retrieving a specific station from the database based on the provided station id
    station = db.query(Station).filter(Station.id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station

@router.delete("/{station_id}", status_code=204)
def delete_station(station_id:int, db: Session = Depends(get_db)):
    # Retrieve the station to be deleted from the database
    station = db.query(Station).filter(Station.id == station_id).first()
    if not station: 
        raise HTTPException(status_code=404, detail="Station not found")
    
    db.delete(station)
    db.commit()

    return Response(status_code=204)