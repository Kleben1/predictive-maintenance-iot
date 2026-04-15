import pandas as pd 
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

def generate_historical_data(n_samples=1000):
    """
    Generate historical data of 1000 samples for training the anomaly detection model.
    """
    print(f"Generation of {n_samples} samples of historical data...")

    # Generate normal data
    normal_temp = np.random.normal(45.0, 5.0, int(n_samples * 0.95))
    normal_vib = np.random.normal(0.5, 0.1, int(n_samples * 0.95))

    # Generate anomaly data
    anomaly_temp = np.random.normal(60.0, 10.0, int(n_samples * 0.05))
    anomaly_vib = np.random.normal(1.0, 0.2, int(n_samples * 0.05))

    # Concatenate normal and anomaly data
    temperatures = np.concatenate([normal_temp, anomaly_temp])
    vibrations = np.concatenate([normal_vib, anomaly_vib])

    # Create DataFrame
    dataframe = pd.DataFrame({
        'temperature': temperatures,
        'vibration': vibrations
    })

    return dataframe

def train_and_save_model():
    
    #Take the historical data
    df = generate_historical_data()

    # Initialize model
    print("Training the model...")
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)

    #Train model
    model.fit(df[['temperature', 'vibration']])
    print("Model trained successfully!")

    #Save model
    api_folder = os.path.join(os.path.dirname(__file__), '..', 'api')
    os.makedirs(api_folder, exist_ok=True)
    model_path = os.path.join(api_folder, 'isolation_forest_model.pkl')

    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()
   