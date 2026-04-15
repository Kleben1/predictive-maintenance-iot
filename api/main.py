from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI(
    title="predictive maintenance API",
    description="API receiving IoT data and predicting failures",
    version="1.0"
)

#Tables creation on startup
database.Base.metadata.create_all(bind=database.engine)

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Data contract to make sure data is correct
class SensorData(BaseModel):
    machine_id: str
    timestamp: str
    temperature: float
    vibration: float

# Health check endpoint
@app.get("/")
def read_root():
    return {"status": "API is running"}

# Predictive endpoint
@app.post("/predict")
def predict_anomaly_and_store(data: SensorData, db: Session = Depends(get_db)):

    """
    Receive sensor data and predict if it's normal or anomaly
    """
    # TODO : load model Scikit-Learn (ISOLATION FOREST)
    is_anomaly = False

    if data.temperature > 80.0 or data.vibration > 4.0:
        is_anomaly = True

    new_prediction = models.PredictionRecord(
        machine_id = data.machine_id,
        timestamp = data.timestamp,
        temperature = data.temperature,
        vibration = data.vibration,
        is_anomaly = is_anomaly
    )

    # Save prediction to database
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    # Draw result to console in order to follow the prediction
    status = "ANOMALY DETECTED 🔴" if is_anomaly else "NORMAL 🟢"
    print(f"[PREDICTION] {data.machine_id} | Temp: {data.temperature}°C | Vibration: {data.vibration}mm/s | Status: {status}")

    # Return prediction result
    return {"status": "saved", "is_anomaly": is_anomaly}

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.PredictionRecord).all()