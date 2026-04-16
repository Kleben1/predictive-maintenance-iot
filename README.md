# 🏭 IoT Predictive Maintenance System

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Isolation_Forest-FF6F00.svg)](https://scikit-learn.org/)

> An end-to-end industrial anomaly detection solution combining real-time IoT data, Artificial Intelligence, and interactive monitoring.

---

## 🌟 Project Overview

This project simulates a smart factory environment where sensors (Temperature & Vibration) stream continuous data. A Machine Learning model analyzes this data stream to predict equipment failures before they happen, displayed on an interactive, real-time control tower.

### 📸 Dashboard Preview
*(Replace the line below with your actual screenshot path)*
<img width="1830" height="714" alt="capture 1" src="https://github.com/user-attachments/assets/56b75fad-d13d-4420-b47d-cd2d840d011e" />
<img width="1789" height="815" alt="capture 2" src="https://github.com/user-attachments/assets/c2e44d51-01d6-41f1-9b97-20f3326d55d5" />

---

## 🧠 Explainable AI (XAI)

Moving beyond traditional "black-box" models, my simulator integrates an explainability layer. The **Isolation Forest** algorithm detects abnormal behaviors, and the business logic instantly provides the root cause:
-  **Critical Overheating**
-  **Abnormal Mechanical Vibrations**
-  **Unusual Temp/Vib Ratios**

---

## 🛠️ Technical Architecture

The project is built using a microservices-oriented architecture, fully containerized:

1. **IoT Simulator**: Generates realistic sensor data streams and randomly injects critical anomalies.
2. **Backend API (FastAPI)**: The core system. Ingests data, queries the ML model, and archives predictions.
3. **ML Brain (Scikit-Learn)**: An unsupervised Machine Learning model trained for outlier detection.
4. **Database (SQLite)**: Persistent storage for historical machine performance and alerts.
5. **Dashboard (Streamlit & Plotly)**: A responsive UI featuring real-time data refresh and smart zoom capabilities for investigation.

---

## 🚀 Quick Start (Docker Mode)

The entire architecture is containerized. **One command** is all it takes to spin up the factory on your local machine.

**Prerequisite:** Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.

```bash
# 1. Clone the repository
git clone [https://github.com/your-username/detecteur-anomalies-production.git](https://github.com/your-username/detecteur-anomalies-production.git)
cd detecteur-anomalies-production

# 2. Launch the entire architecture
docker compose up --build -d

Once the containers are running, access the services:

📊 Live Dashboard: http://localhost:8501

⚙️ API Documentation: http://localhost:8000/docs

📈 Advanced Features
[x] Live Monitoring: "Electrocardiogram" style visualization of sensor data.

[x] Investigation Mode: Toggle real-time updates off to freeze the chart and zoom into specific anomalies.

[x] Auto-Scaling: Plotly charts dynamically adapt to data variance without layout jumps.

[x] Docker Resilience: Cross-container networking and automatic state recovery.

🧪 Tech Stack
Language: Python 3.13

Data & ML: Pandas, Scikit-Learn, Joblib

Backend: FastAPI, Uvicorn, SQLAlchemy

Frontend / Dataviz: Streamlit, Plotly

DevOps: Docker, Docker Compose
