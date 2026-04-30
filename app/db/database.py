from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a local file named ev_charging.db for SQLite database
DATABASE_URL = "sqlite:///./ev_charging.db"

#Creating the engine 
#connet_args={"check_same_thread": False} is required for SQLite in FastAPI to prevent thread issues
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Future database model will inherit from this Base class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()