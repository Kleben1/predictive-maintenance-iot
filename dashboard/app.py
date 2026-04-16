import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go 
import time

# Page configuration
st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# API configuration$
API_URL = "http://127.0.0.1:8000/history"

def fetch_data():
    # Fetch data from API and return a pandas DataFrame
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                # Convert timestamp to datetime
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
    return pd.DataFrame()

# Dashboard title
st.title("Predictive Maintenance Dashboard")
st.markdown("This dashboard displays real-time data from the predictive maintenance system.")

# Grab data from API
df = fetch_data()

if not df.empty:
    header_col1, header_col2 = st.columns([3, 1])
    # Live Metrics
    with header_col1:
        st.subheader("Live Metrics")

    with header_col2:
        live_update = st.toggle("Update data every 2 seconds", value=False)

    # Get Lastes Data
    latest_data = df.iloc[-1]

    # Create columns for metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Actual Temperature", f"{latest_data['temperature']} °C")
    col2.metric("Actual Vibration", f"{latest_data['vibration']} mm/s")

    # Retrocontrol
    if latest_data['is_anomaly']:
        raw_reason = latest_data.get('reason')
        reason = raw_reason if pd.notna(raw_reason) and raw_reason else "Critical Anomaly"
        col3.error(f"ALERT : {reason}")
    else:
        col3.success("NORMAL OPERATION")

    # Draw charts
    st.markdown("---")
    st.subheader("Historical Data (Last 60 records)")

    # Get Last 60 records
    df_last_60 = df.tail(60)

    # Grab anomalies in the last 60 records
    anomaly_data_60 = df_last_60[df_last_60['is_anomaly'] == True]
    
    # Create Plotly (Temperature)
    fig_temp = go.Figure()
    # Blue line for global temperature
    fig_temp.add_trace(go.Scatter(x=df_last_60['timestamp'], y=df_last_60['temperature'], mode='lines', name='Temperature', line=dict(color='blue', width=1)))
    # Red points for anomalies
    fig_temp.add_trace(go.Scatter(x=anomaly_data_60['timestamp'], y=anomaly_data_60['temperature'], mode='markers', name='Anomaly 🔴', marker=dict(color='red', size=8, symbol='x')))
    fig_temp.update_layout(
        title="Temperature Evolution", 
        xaxis_title="Time", 
        yaxis_title="°C",
        yaxis=dict(range=[20, 110]),
        height=300,
        template="plotly_white", 
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig_temp, use_container_width=True)

    # Create Plotly (Vibration)
    fig_vib = go.Figure()
    # Green line for global vibration
    fig_vib.add_trace(go.Scatter(x=df_last_60['timestamp'], y=df_last_60['vibration'], mode='lines', name='Vibration', line=dict(color='green', width=1)))
    # Red points for anomalies
    fig_vib.add_trace(go.Scatter(x=anomaly_data_60['timestamp'], y=anomaly_data_60['vibration'], mode='markers', name='Anomaly 🔴', marker=dict(color='red', size=8, symbol='x')))
    fig_vib.update_layout(
        title="Vibration Evolution", 
        xaxis_title="Time", 
        yaxis_title="mm/s",
        yaxis=dict(range=[0, 3]),
        height=300, 
        template="plotly_white",
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig_vib, use_container_width=True)

    # History of alerts
    with st.expander("📄 See the complete history of alerts"):
        all_anomalies = df[df['is_anomaly'] == True]
        if not all_anomalies.empty:
            cols = ['timestamp', 'machine_id', 'temperature', 'vibration']
            if 'reason' in all_anomalies.columns:
                cols.append('reason')
            st.dataframe(all_anomalies.sort_values(by='timestamp', ascending=False)[cols], use_container_width=True)
        else:
            st.write("No anomaly detected for the moment. Good job maintenance team!")
else:
    st.warning("⏳ Waiting for data from the API... Check that the simulator and the API are launched.")

# 4. Refresh loop
if live_update:
    time.sleep(2)
    st.rerun()
