from sqlalchemy import Column, Integer, String, Boolean
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