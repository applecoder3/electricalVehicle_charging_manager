from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.database import Base

#This class defines the structure of the sessions table in the database
class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("stations.id"), nullable=False)

    # Tracking the battery percentage and time of the session
    start_time = Column(DateTime, default=datetime.now(timezone.utc))
    end_time = Column(DateTime, nullable=True)

    start_battery_level = Column(Integer)
    ending_battery_percentage = Column(Integer, nullable=True)

    # This will tell sqlalchemy to connect this class to the Station class based on the station_id foreign key
    station = relationship("Station", back_populates="sessions")