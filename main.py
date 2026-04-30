from fastapi import FastAPI

# wiring up the API route from app.api station to the main application
from app.api import stations

from app.db.database import engine, Base
from app.models.station import Station

# Tells SQLAlchemy to create the tables in the database based on the models defined in the code
Base.metadata.create_all(bind=engine)

app = FastAPI(title="EV Charging Manager API")

# Plug the router into the main application 
# Add a prefix so every endpoint in stations file starts with /stations

app.include_router(stations.router, prefix="/stations", tags=["Stations"])

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/health")
def health_check():
    return {"status": "API is online", "version": "1.0.0"}
