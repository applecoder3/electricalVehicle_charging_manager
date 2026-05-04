from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

#This class defines the structure of the stations table in the database




class Station(Base):
    # Define the table name for this model 
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    is_online = Column(Boolean, default=True)
    current_status = Column(String, default="Available")

    # This will tell sqlalchemy to connect this class to the Session class based on the station_id foreign key. if a station is deleted, all related sessions will also be deleted
    sessions = relationship("Session", back_populates="station", cascade="all, delete-orphan")