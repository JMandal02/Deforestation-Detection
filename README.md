# 🔥 Classification of Fire Types in India Using MODIS Satellite Data (2021–2023)


This project focuses on detecting and classifying fire events across India using thermal anomaly data from NASA's MODIS (Moderate Resolution Imaging Spectroradiometer) satellite sensors. The classification includes vegetation fires, agricultural burns, volcanic activity, and offshore/static thermal sources.


## Demo 🚀
Live Deployment:[https://deforestation-detection.streamlit.app/](https://deforestation-detection.streamlit.app/)

## 📦 Model Access

Due to GitHub's file size limit (25 MB), the trained model (`best_fire_detection_model.pkl`, 460.1 MB) is hosted on Google Drive.

👉 **[Download the trained model here](https://drive.google.com/drive/folders/1ub_ktWHXdvv2kn104xwa1QrYq2Z0_DM3?usp=sharing)**


## 📌 Objective

Leverage MODIS data from **2021 to 2023** to develop a **machine learning model** that identifies the source of thermal anomalies. This is crucial for:

-  Environmental and deforestation monitoring
-  Real-time disaster response
-  Data-driven resource management
-  Long-term ecological analysis

## 🚀 Features

-  **Accurate classification**: Vegetation, volcano, static land, offshore fire types
-  **Geospatial data integration**: MODIS thermal readings with location data
- 🛰 **Dual satellite source**: Aqua (PM) and Terra (AM) observations
- **Interactive and reproducible ML pipeline**
- 🇮🇳 **Country-specific focus**: India dataset (2021–2023)



> ✅ **For Students:** If your model file is large, upload it to Google Drive and add the link to your `README.md`, just like this example.

## 🌍 Project Overview

India experiences thousands of fire incidents annually, ranging from wildfires to agricultural burns. While MODIS provides rich thermal and geospatial data, classifying fire types remains a significant challenge.

This project addresses the challenge by:

- Preprocessing MODIS fire data (2021–2023)
- Engineering thermal, temporal, and geospatial features
- Training ML models to classify fire sources
-  Building a scalable and reusable ML pipeline

## 🗃️ MODIS Dataset Summary

| Attribute | Description |
|-----------|-------------|
| **Sensor** | MODIS (Moderate Resolution Imaging Spectroradiometer) |
| **Satellites** | Terra (AM) and Aqua (PM) |
| **Resolution** | 1 km per pixel |
| **Frequency** | 2–4 observations per day |
| **Source** | NASA FIRMS |

## 🔍 Fire Detection Mechanism

MODIS detects thermal anomalies using contextual algorithms across multiple spectral bands:

- 🔸 **Bands 21/22** – Mid-infrared for fire detection
- 🔸 **Band 31** – Thermal infrared for surface temperature


> 🔧 **Note:** NRT (Near Real-Time) data may contain minor spatial inaccuracies due to orbit estimation.

## 📊 Key MODIS Data Parameters

| Column Name | Description |
|-------------|-------------|
| `latitude` | Center of the 1 km fire pixel (Y-axis) |
| `longitude` | Center of the 1 km fire pixel (X-axis) |
| `bright_t31` | Brightness temperature from Band 31 (Kelvin) |
| `bright_t14` | Brightness temperature from Band 21/22 |
| `scan` | Pixel width on ground |
| `track` | Pixel height on ground |
| `acq_date` | Date of acquisition |
| `acq_time` | Time of acquisition (UTC) |
| `satellite` | Aqua or Terra |
| `confidence` | Detection certainty (low, nominal, high) |
| `version` | Data processing version |
| `frp` | Fire Radiative Power (MW) |
| `type` | Fire source (0=Vegetation, 1=Volcano, 2=Static, 3=Offshore) |
| `daynight` | D = Day, N = Night |

## 💻 Installation & Setup

### Prerequisites

- Python 3.8 or above
- Jupyter Notebook or any Python IDE

### Required Libraries

Install the required packages using pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn geopandas jupyter
```

Alternatively, install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Quick Start

1. Clone this repository:
   ```bash
   git clone [your-repository-url]
   cd fire-classification-modis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the trained model from the Google Drive link above

4. Run the Jupyter notebooks to explore the data and model

## 📁 Project Structure

```
fire-classification-modis/
├── data/                    # Raw and processed data
├── notebooks/               # Jupyter notebooks for analysis
├── src/                     # Source code
├── models/                  # Model files (download separately)
└──requirements.txt          # Python dependencies

```

## 🔬 Methodology

1. **Data Preprocessing**: Clean and filter MODIS thermal anomaly data for India
2. **Feature Engineering**: Extract temporal, thermal, and geospatial features
3. **Model Training**: Train classification models to distinguish fire types
4. **Evaluation**: Assess model performance using appropriate metrics
5. **Deployment**: Create a reusable pipeline for fire type classification

## 📈 Results

The trained model achieves high accuracy in classifying fire types across India, providing valuable insights for environmental monitoring and disaster response applications.

## ✍️ Contributing

Contributions are welcome! Feel free to:

- Fork this repository
- Open issues for bugs or feature requests
- Submit pull requests for improvements

Areas for contribution:
- Model improvement and optimization
- Enhanced data preprocessing
- Advanced visualization techniques
- Real-time data integration


## 🙋‍♂️ Acknowledgments

- **NASA FIRMS** for providing open access to MODIS fire data
- The open-source community for the tools and libraries used


> **Note:** All data used in this project is publicly available from NASA FIRMS. For installation issues, refer to the dependencies listed in `requirements.txt`.
