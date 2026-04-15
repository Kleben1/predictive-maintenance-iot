from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI(
    title="predictive maintenance API",
    description="API receiving IoT data and predicting failures",
    version="1.0"
)

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
def predict_anomaly(data: SensorData):
    """
    Receive sensor data and predict if it's normal or anomaly
    """
    
    # TODO : load model Scikit-Learn (ISOLATION FOREST)
    is_anomaly = False

    if data.temperature > 80.0 or data.vibration > 4.0:
        is_anomaly = True

    # Draw result to console in order to follow the prediction
    status = "ANOMALY DETECTED" if is_anomaly else "NORMAL"
    print(f"[PREDICTION] {data.machine_id} | Temp: {data.temperature}°C | Vibration: {data.vibration}mm/s | Status: {status}")

    # Return prediction result
    return {
        "machine_id": data.machine_id,
        "timestamp": data.timestamp,
        "temperature": data.temperature,
        "vibration": data.vibration,
        "status": status
    }