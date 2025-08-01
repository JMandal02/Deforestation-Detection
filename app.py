import streamlit as st
import numpy as np
import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import gdown
import joblib  # or pickle
import os


# Configure page
st.set_page_config(
    page_title="MODIS Fire Classification - India",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .project-info {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
    }
            
    
    
    .info-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff6b35;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
    }
    
    .stNumberInput > div > div > input {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# # Load model and scaler with error handling
# @st.cache_resource
# def load_models():
#     try:
#         model = joblib.load("best_fire_detection_model.pkl")
#         scaler = joblib.load("scaler.pkl")
#         return model, scaler
#     except FileNotFoundError as e:
#         st.error(f"Model files not found: {e}")
#         st.stop()
#     except Exception as e:
#         st.error(f"Error loading models: {e}")
#         st.stop()

# model, scaler = load_models()


# Google Drive File IDs
MODEL_FILE_ID = "1eUd35Wd8TanFKvur-bbnRo0BEJv_97Ae"
SCALER_FILE_ID = "1WB-nBR3UhXDdZtxgWJmcPzhbm5IDo7lV"

# Local filenames
MODEL_FILE = "best_fire_detection_model.pkl"
SCALER_FILE = "scaler.pkl"

# Download function
def download_from_drive(file_id, output):
    url = f"https://drive.google.com/uc?id={file_id}"
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

# Load model and scaler with error handling
@st.cache_resource
def load_models():
    try:
        download_from_drive(MODEL_FILE_ID, MODEL_FILE)
        download_from_drive(SCALER_FILE_ID, SCALER_FILE)

        model = joblib.load(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
        return model, scaler

    except FileNotFoundError as e:
        st.error(f"Model files not found: {e}")
        st.stop()
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

# Load them
model, scaler = load_models()

# Header
st.markdown("""
<div class="main-header">
    <h1>🛰️ MODIS Fire Type Classification System</h1>
    <h3>Classification of Fire Types in India Using MODIS Satellite Data (2021–2023)</h3>
</div>
""", unsafe_allow_html=True)



# Project Information
st.markdown("""
<div class="project-info">
    <h3>🌍 Project Overview</h3>
    <p style="color: white; font-size: 1.1rem; margin-bottom: 1.5rem;">This system classifies thermal anomalies detected by NASA's MODIS sensors across India, helping identify different fire sources for environmental monitoring, disaster response, and ecological analysis.</p>
    <div style="display: flex; justify-content: space-around; margin-top: 1rem; flex-wrap: wrap; gap: 1rem;">
        <div style="color: white; text-align: center;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-weight: bold;">📊 Dataset:</span>
            <span style="color: #FFD700; font-weight: bold; margin-left: 0.5rem;">2021-2023</span>
        </div>
        <div style="color: white; text-align: center;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-weight: bold;">🛰️ Satellites:</span>
            <span style="color: #FFD700; font-weight: bold; margin-left: 0.5rem;">Terra & Aqua</span>
        </div>
        <div style="color: white; text-align: center;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-weight: bold;">📍 Coverage:</span>
            <span style="color: #FFD700; font-weight: bold; margin-left: 0.5rem;">India</span>
        </div>
        <div style="color: white; text-align: center;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 15px; font-weight: bold;">🔍 Resolution:</span>
            <span style="color: #FFD700; font-weight: bold; margin-left: 0.5rem;">1km/pixel</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar for input parameters
st.sidebar.header("🛰️ MODIS Parameters")
st.sidebar.markdown("Enter the satellite readings for fire classification:")

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input section in main area
    st.subheader("🔥 MODIS Thermal Anomaly Data")
    
    # Create input columns
    input_col1, input_col2 = st.columns(2)
    
    with input_col1:
        brightness = st.number_input(
            "🌡️ Brightness (Band 21/22) - Kelvin",
            min_value=250.0,
            max_value=500.0,
            value=320.0,
            step=0.1,
            help="Fire detection brightness temperature from MODIS mid-infrared bands"
        )
        
        frp = st.number_input(
            "🔥 Fire Radiative Power (MW)",
            min_value=0.0,
            max_value=1000.0,
            value=25.0,
            step=0.1,
            help="Fire Radiative Power - measure of fire intensity in Megawatts"
        )
        
        scan = st.number_input(
            "📏 Scan (Pixel Width)",
            min_value=0.5,
            max_value=5.0,
            value=1.0,
            step=0.1,
            help="Pixel width on the ground (km)"
        )
    
    with input_col2:
        bright_t31 = st.number_input(
            "🌡️ Brightness T31 (Band 31) - Kelvin",
            min_value=250.0,
            max_value=400.0,
            value=295.0,
            step=0.1,
            help="Surface temperature from MODIS thermal infrared Band 31"
        )
        
        track = st.number_input(
            "📏 Track (Pixel Height)",
            min_value=0.5,
            max_value=5.0,
            value=1.0,
            step=0.1,
            help="Pixel height on the ground (km)"
        )
        
        confidence = st.selectbox(
            "✅ Detection Confidence",
            options=["low", "nominal", "high"],
            index=1,
            help="Certainty of fire detection by MODIS algorithm"
        )

with col2:
    # Information panel
    st.subheader("ℹ️ MODIS Fire Detection")
    
    st.markdown("""
    <div class="info-box">
        <h4>About MODIS</h4>
        <p>MODIS uses contextual algorithms across thermal channels to detect fire pixels with 2-4 observations per day from Terra and Aqua satellites.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fire type information
    with st.expander("🔥 Fire Type Categories"):
        st.markdown("""
        - **Type 0 - Vegetation Fire**: Forest fires, grassland burns, natural wildfires
        - **Type 1 - Volcano**: Volcanic thermal activity (rare in India)  
        - **Type 2 - Static Land Source**: Industrial fires, gas flares, urban fires
        - **Type 3 - Offshore**: Maritime fires, coastal thermal sources
        """)
    
    # Parameter explanations
    with st.expander("📖 Parameter Guide"):
        st.markdown("""
        - **Brightness**: Mid-infrared temperature for fire detection
        - **Brightness T31**: Thermal infrared surface temperature
        - **FRP**: Radiant heat energy output from fire
        - **Scan/Track**: Ground pixel dimensions
        - **Confidence**: Algorithm certainty level
        """)

# Prediction section
st.markdown("---")
st.subheader("🎯 Fire Type Classification")

# Create prediction button with better styling
predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])

with predict_col2:
    predict_button = st.button(
        "🔍 Classify Fire Type",
        type="primary",
        use_container_width=True
    )

if predict_button:
    # Map confidence to numeric
    confidence_map = {"low": 0, "nominal": 1, "high": 2}
    confidence_val = confidence_map[confidence]
    
    # Prepare input data (6 features as per original model)
    input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])
    
    try:
        # Scale input
        scaled_input = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(scaled_input)[0]
        
        # Fire type mapping based on MODIS classification
        fire_types = {
            0: "Vegetation Fire",
            1: "Volcano",
            2: "Static Land Source", 
            3: "Offshore"
        }
        
        fire_descriptions = {
            0: "🌿 Natural vegetation fires - forests, grasslands, agricultural burns",
            1: "🌋 Volcanic thermal activity (rare in Indian subcontinent)",
            2: "🏭 Industrial fires, gas flares, urban thermal sources",
            3: "🌊 Maritime fires, offshore platforms, coastal thermal activity"
        }
        
        fire_contexts = {
            0: "Common during dry seasons, particularly in forest areas and agricultural regions",
            1: "Typically associated with volcanic regions - uncommon in India",
            2: "Often related to industrial activities, refineries, or urban fire incidents", 
            3: "Usually occurs in coastal areas, shipping lanes, or offshore installations"
        }
        
        result = fire_types.get(prediction, "Unknown")
        description = fire_descriptions.get(prediction, "Unknown fire type")
        context = fire_contexts.get(prediction, "")
        
        # Display results
        st.markdown(f"""
        <div class="prediction-box">
            <h2>🔥 Predicted Fire Type: {result}</h2>
            <p>{description}</p>
            <p><em>{context}</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show input values summary
        st.subheader("📋 MODIS Data Summary")
        summary_col1, summary_col2, summary_col3 = st.columns(3)
        
        with summary_col1:
            st.metric("🌡️ Brightness", f"{brightness} K", help="Mid-infrared temperature")
            st.metric("🌡️ Brightness T31", f"{bright_t31} K", help="Thermal infrared temperature")
        
        with summary_col2:
            st.metric("🔥 Fire Radiative Power", f"{frp} MW", help="Fire intensity measure")
            st.metric("✅ Confidence", confidence.title(), help="Detection certainty")
        
        with summary_col3:
            st.metric("📏 Scan", f"{scan} km", help="Pixel width")
            st.metric("📏 Track", f"{track} km", help="Pixel height")
        
        # Visualization of input parameters
        st.subheader("📊 MODIS Parameter Analysis")
        
        # Create radar chart
        parameters = ['Brightness\n(normalized)', 'Brightness T31\n(normalized)', 'Fire Radiative\nPower', 'Scan', 'Track', 'Confidence\nLevel']
        values = [
            min(brightness/400*100, 100), 
            min(bright_t31/350*100, 100), 
            min(frp/100*100, 100),
            scan/5*100, 
            track/5*100, 
            confidence_val/2*100
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=parameters,
            fill='toself',
            name='Current Readings',
            line_color='#ff6b35',
            fillcolor='rgba(255, 107, 53, 0.3)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    ticksuffix="%"
                )),
            showlegend=True,
            title="MODIS Parameter Profile",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Additional insights
        st.subheader("🔍 Classification Insights")
        
        insight_col1, insight_col2 = st.columns(2)
        
        with insight_col1:
            st.markdown("**🌡️ Temperature Analysis**")
            temp_diff = brightness - bright_t31
            if temp_diff > 50:
                st.success("High temperature differential suggests active fire")
            elif temp_diff > 20:
                st.warning("Moderate temperature differential")
            else:
                st.info("Low temperature differential - possible smoldering")
        
        with insight_col2:
            st.markdown("**🔥 Fire Intensity**")
            if frp > 50:
                st.error("High intensity fire - immediate attention required")
            elif frp > 20:
                st.warning("Moderate intensity fire")
            else:
                st.info("Low intensity thermal anomaly")
        
    except Exception as e:
        st.error(f"Error making prediction: {e}")

# Dataset Information
st.markdown("---")
st.subheader("📊 Dataset Information")

dataset_col1, dataset_col2 = st.columns(2)

with dataset_col1:
    st.markdown("""
    **🛰️ MODIS Satellite Specifications**
    - **Sensors**: Terra (AM) & Aqua (PM) satellites
    - **Spatial Resolution**: 1 km per pixel
    - **Temporal Coverage**: 2021-2023
    - **Observation Frequency**: 2-4 times daily
    - **Geographic Focus**: India
    """)

with dataset_col2:
    st.markdown("""
    **🔍 Fire Detection Channels**
    - **Bands 21/22**: Mid-infrared fire detection
    - **Band 31**: Thermal infrared surface temperature
    - **Algorithm**: Contextual fire detection
    - **Data Source**: NASA FIRMS
    - **Processing**: Near Real-Time (NRT)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🛰️ Powered by NASA MODIS satellite data • 🇮🇳 Focused on India (2021-2023)</p>
    <p>🌿 AICTE Internship Project - Cycle 2 • Built for Environmental Monitoring & Disaster Response</p>
</div>
""", unsafe_allow_html=True)

# Sidebar additional info
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔥 MODIS Fire Types")
st.sidebar.markdown("""
- **Type 0**: Vegetation Fire 🌿
- **Type 1**: Volcano 🌋
- **Type 2**: Static Land Source 🏭  
- **Type 3**: Offshore 🌊
""")

st.sidebar.markdown("### 🎯 Project Goals")
st.sidebar.info("""
- Environmental monitoring
- Real-time disaster response  
- Data-driven resource management
- Long-term ecological analysis
""")

st.sidebar.markdown("### 📈 Model Performance")
st.sidebar.success("Trained on 2021-2023 India MODIS data with optimized classification accuracy")