from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime, timezone
import database

class PredictionRecord(database.Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String)
    timestamp = Column(String)
    temperature = Column(Float)
    vibration = Column(Float)
    is_anomaly = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
