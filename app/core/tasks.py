import os
from celery import Celery
from datetime import datetime, timezone
from app.db.database import SessionLocal
from app.models.session import Session as SessionModel
from app.models.station import Station

""" Initialize the Celery App using the Redist URL from the docker yaml file"""
redis_url = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
celery_app = Celery("ev_tasks", broker=redis_url)

"""Configure the Beat Scheduler 
    for testing this will be set to run every 60 seconds
"""

celery_app.conf.beat_schedule = {
    'simulate-charging-every-minute':{
        'task': 'simulate_charging_task',
        'schedule': 60.0,
    },
}
celery_app.conf.timezone = 'UTC'

"""The Background Task"""
@celery_app.task(name='simulate_charging_task')
def simulate_charging():
    #Background job is to increase battery level for all active sessions by 10%

    db = SessionLocal()
    try:
        #Finding active sessions (end time is still Null)
        active_sessions = db.query(SessionModel).filter(SessionModel.end_time == None).all()

        if not active_sessions:
            return "No active sessions to charge"
        
        for session in active_sessions:
            #If the end battery is None start from the starting battery level
            current_battery = session.ending_battery_percentage if session.ending_battery_percentage is not None else session.start_battery_level

            new_battery = current_battery + 10

            if new_battery >= 100:
                session.ending_battery_percentage = 100
                session.end_time = datetime.now(timezone.utc)

                station = db.query(Station).filter(Station.id == session.station_id).first()
                if station:
                    station.current_status = "Available"
            else:
                session.ending_battery_percentage = new_battery

        db.commit()
        return f"Processed {len(active_sessions)} active charging sessions."
    
    except Exception as e:
        db.rollback()
        print(f"Error in backgorund task: {e}")
    finally:
        db.close()