from fastapi import APIRouter, Depends, HTTPException
from app.schemas.station import StationResponse

# Initialize the router for this file
router = APIRouter()

# mock data base for testing 
MOCK_DB ={
    1: {"id": 1, "name": "Station A", "location": "london", 
        "is_online": True, "current_status": "available"},
    2: {"id": 2, "name": "Station B", "location": "paris", 
        "is_online": True, "current_status": "occupied"}
}

@router.get("/stations/{station_id}", response_model=StationResponse)
def get_station(station_id: int):
    # retrieving station from the mock database
    station = MOCK_DB.get(station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    
    return station