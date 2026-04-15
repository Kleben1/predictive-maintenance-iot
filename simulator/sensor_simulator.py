import time
import random
import json
import os  
import requests
from datetime import datetime

# Grap api url via environment variable
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

def generate_sensor_data(machine_id="MACHINE_001"):
    """
    Generate realistic sensor data for a machine ID
    Generate normal data with 90% probability
    Generate anomaly data with 10% probability
    """
    
    # Timestamp generation in ISO format
    timestamp = datetime.utcnow().isoformat()

    #Anomaly probability (10%)
    is_anomaly = random.random() < 0.10

    if is_anomaly:
        #Abnormal values : temperature and vibrations
        temperature = random.uniform(85.0, 105.0) #High temperature
        vibration = random.uniform(1.5, 3.0) #High vibration
        print(f" [SIMULATION] Anomaly generated for {machine_id} !")
    else:
        #Normal values
        temperature = random.normalvariate(45.0, 5.0) #Sum 45°C +/- 5°C
        vibration = random.normalvariate(1.2, 0.3) #Sum 1.2mm/s +/- 0.3mm/s
    
    return {
        "machine_id": machine_id,
        "timestamp": timestamp,
        "temperature": round(temperature, 2),
        "vibration": round(vibration, 2)
    }

def run_simulator():
    print("Starting sensor simulator...")
    print(f"Sending data API at {API_URL}")

    while True:
        # Generate sensor data
        data = generate_sensor_data()

        # Draw data to console
        print(f"[{data["timestamp"]}] {data["temperature"]}°C | {data["vibration"]}mm/s")

        # Send data to API
        try:
            response = requests.post(API_URL, json=data)
            if response.status_code == 200:
                print("Data sent successfully and will be analysed")
        except requests.exceptions.ConnectionError:
            print("Failed to connect to API. Ensure the FastAPI server is running.")
        
        # Wait 2 seconds before next reading
        time.sleep(2)

if __name__ == "__main__":
    try:
        run_simulator()
    except KeyboardInterrupt:
        print("\nSimulator stopped by user")