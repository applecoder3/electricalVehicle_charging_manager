from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#New imnport for the migration to PostgresSql
import os



#Tells python to look for the Database_url environment variable that was set in docker-compose
#If it can't find it. it defaults back to SQLite as a safety net
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ev_database.db")

engine = create_engine(SQLALCHEMY_DATABASE_URL)





# Create a local file named ev_charging.db for SQLite database
#DATABASE_URL = "sqlite:///./ev_charging.db"

#Creating the engine 
#connet_args={"check_same_thread": False} is required for SQLite in FastAPI to prevent thread issues
#engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Future database model will inherit from this Base class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()