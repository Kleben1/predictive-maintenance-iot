from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Initialize FastAPI
app = FastAPI(
    title="predictive maintenance API",
    description="API receiving IoT data and predicting failures",
    version="2.0"
)

#Tables creation on startup
database.Base.metadata.create_all(bind=database.engine)

# Load the trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'isolation_forest_model.pkl')

try:
    ia_model = joblib.load(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    ia_model = None

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
    return {"status": "API is running", "ai_ready": ia_model is not None}

# Predictive endpoint
@app.post("/predict")
def predict_anomaly_and_store(data: SensorData, db: Session = Depends(get_db)):

    """
    Receive sensor data and predict if it's normal or anomaly
    """
    # TODO : load model Scikit-Learn (ISOLATION FOREST)
    is_anomaly = False

    if ia_model:
        # Format data for the model
        features = [[data.temperature, data.vibration]]
        df_features = pd.DataFrame(features, columns=['temperature', 'vibration'])

        # Predict
        prediction = ia_model.predict(df_features)

        # -1 = anomaly, 1 = normal
        is_anomaly = bool(prediction[0] == -1)

    # If AI is not available, use a fallback mechanism
    else:
        is_anomaly = data.temperature > 80.0 or data.vibration > 4.0

    # Determine the reason for the anomaly
    reason_text = None
    
    if is_anomaly:
        reasons = []
        if data.temperature > 60.0: reasons.append("Overheating")
        elif data.temperature < 30.0: reasons.append("Under-temperature")
        if data.vibration > 1.8: reasons.append("High vibration")
        elif data.vibration < 0.6: reasons.append("Low vibration")
        
        if not reasons: reasons.append("Unusual Temp/Vib ratio")
        reason_text = " + ".join(reasons)

    # Save prediction to database
    new_prediction = models.PredictionRecord(
        machine_id = data.machine_id,
        timestamp = data.timestamp,
        temperature = data.temperature,
        vibration = data.vibration,
        is_anomaly = is_anomaly,
        reason = reason_text
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    status_print = f"🔴 ANOMALIE ➔ {reason_text}" if is_anomaly else "🟢 NORMAL"
    print(f"[IA] {data.machine_id} | Temp: {data.temperature}°C | Vib: {data.vibration}mm/s | Status: {status_print}")

    return {"status": "saved", "is_anomaly": is_anomaly, "reason": reason_text}

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.PredictionRecord).all()