# 🔥 Classification of Fire Types in India Using MODIS Satellite Data (2021–2023)

**🌿 A Project under AICTE Internship – Cycle 2**

This project focuses on the **detection and classification of fire events** across India using satellite-based thermal anomaly data from NASA’s MODIS (Moderate Resolution Imaging Spectroradiometer) sensors. Fire types include vegetation fires, agricultural burns, volcanic activity, and other static or offshore thermal sources.

By leveraging MODIS data captured between 2021 and 2023, we aim to build a robust **machine learning classification model** capable of identifying the underlying **source of thermal anomalies**. This classification is essential for supporting:

- 🌲 Environmental and deforestation monitoring  
- 🚨 Real-time disaster response  
- 📊 Data-driven resource management  
- 🔍 Long-term ecological analysis


## 🌍 Overview

India experiences thousands of fire incidents annually — from natural wildfires in forests to human-induced agricultural burns. While NASA's MODIS satellites provide rich thermal and geospatial datasets, classifying the **type of fire** based on that data remains a key analytical challenge.

This project solves that problem by:

- Preprocessing MODIS fire data for India (2021–2023)
- Engineering relevant thermal, temporal, and geospatial features
- Training ML models to accurately classify fire types (vegetation, volcano, etc.)
- Providing a scalable pipeline for real-world applications in fire detection


## 🚀 Features

- 🔎 **Accurate Classification** of fire source types (vegetation, volcano, static land source, offshore).
- 🌐 **Geospatial Data Integration** from MODIS satellite captures.
- 🛰️ Utilizes both **Aqua** and **Terra** satellite data.
- 📊 Interactive and Reproducible ML pipeline for data preprocessing, training, and evaluation.
- 📍 Country-specific focus: **India**, 2021–2023 dataset.

## 📦 MODIS Dataset Summary

- **Sensor**: MODIS (Moderate Resolution Imaging Spectroradiometer)
- **Satellites**: Terra (AM overpass) and Aqua (PM overpass)
- **Resolution**: 1 km per pixel
- **Frequency**: 2–4 observations/day
- **Source**: [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)

## 🔍 Fire Detection Mechanism

MODIS detects thermal anomalies using contextual algorithms across three key channels:
- **Bands 21/22**: Fire detection (mid-infrared)
- **Band 31**: Surface temperature (thermal infrared)

Pixels are classified into:
- Fire
- Non-fire
- Water
- Cloud
- Unknown
- Missing

> 🔧 Note: NRT (Near Real-Time) data may have minor spatial inaccuracies due to orbit estimation.

## 🧾 Important Parameters in MODIS Data

| Column Name | Description |
|-------------|-------------|
| `latitude` | Center of nominal 1 km fire pixel |
| `longitude` | Center of nominal 1 km fire pixel |
| `bright_t31` | Brightness temperature from MODIS Channel 31 (Kelvin) |
| `scan` | Pixel width on the ground |
| `track` | Pixel height on the ground |
| `acq_date` | Acquisition date |
| `acq_time` | Acquisition time (UTC) |
| `satellite` | Either `Aqua` or `Terra` |
| `confidence` | Certainty of fire detection: `low`, `nominal`, `high` |
| `version` | Data processing version (e.g., `6.0NRT`) |
| `bright_t14` | Brightness temperature from thermal infrared Band 21/22 |
| `frp` | Fire Radiative Power (MW) |
| `type` | Thermal anomaly source: `0` = Vegetation, `1` = Volcano, `2` = Static Land Source, `3` = Offshore |
| `daynight` | `D` = Day, `N` = Night observation |

## 💻 Installation

### 📋 Prerequisites

- Python 3.8+
- pip
- Jupyter Notebook or any Python IDE

### 📦 Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn geopandas jupyter
