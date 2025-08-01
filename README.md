# 🔥 Classification of Fire Types in India Using MODIS Satellite Data (2021–2023)

🌿 **AICTE Internship – Cycle 2 Project**

This project focuses on detecting and classifying fire events across India using thermal anomaly data from NASA’s MODIS (Moderate Resolution Imaging Spectroradiometer) satellite sensors. The classification includes:

- 🌲 Vegetation fires  
- 🌾 Agricultural burns  
- 🌋 Volcanic activity  
- 🌊 Offshore/static thermal sources  


## 📌 Objective

Leverage MODIS data from **2021 to 2023** to develop a **machine learning model** that identifies the source of thermal anomalies. This is crucial for:

- 🌳 Environmental and deforestation monitoring  
- 🚨 Real-time disaster response  
- 📈 Data-driven resource management  
- 🧪 Long-term ecological analysis  



## 📦 Model Access

Due to GitHub's file size limit (25 MB), the trained model (`best_fire_detection_model.pkl`, 460.1 MB) is hosted on Google Drive.

👉 **[Click here to download the model](https://drive.google.com/drive/folders/1ub_ktWHXdvv2kn104xwa1QrYq2Z0_DM3?usp=sharing)**

> ✅ **For Students:** If your model file is large, upload it to Google Drive and add the link to your `README.md`, just like this example.



## 🌍 Project Overview

India experiences thousands of fire incidents annually — from wildfires to agricultural burns. While MODIS provides rich thermal and geospatial data, classifying fire types remains a challenge.

This project addresses the challenge by:

- ✅ Preprocessing MODIS fire data (2021–2023)  
- 🧠 Engineering thermal, temporal, and geospatial features  
- 🤖 Training ML models to classify fire sources  
- 🔁 Building a scalable and reusable ML pipeline  



## 🚀 Features

- 🔍 **Accurate classification**: Vegetation, volcano, static land, offshore  
- 🌐 **Geospatial data integration**: MODIS thermal readings  
- 🛰️ **Dual satellite source**: Aqua (PM) and Terra (AM)  
- 📊 **Interactive and reproducible ML pipeline**  
- 🇮🇳 **Country-specific focus**: India (2021–2023 dataset)  



## 🗃️ MODIS Dataset Summary

| Attribute | Description |
|----------|-------------|
| **Sensor** | MODIS (Moderate Resolution Imaging Spectroradiometer) |
| **Satellites** | Terra (AM) and Aqua (PM) |
| **Resolution** | 1 km per pixel |
| **Frequency** | 2–4 observations/day |
| **Source** | NASA FIRMS |


## 🔍 Fire Detection Mechanism

MODIS detects thermal anomalies using contextual algorithms across:

- 🔸 **Bands 21/22** – Mid-infrared for fire detection  
- 🔸 **Band 31** – Thermal infrared for surface temperature  

Pixels are classified into:
- 🔥 Fire  
- 🌊 Water  
- ☁️ Cloud  
- ❓ Unknown  
- 🚫 Missing  
- ❌ Non-fire  

> 🔧 *Note: NRT (Near Real-Time) data may contain minor spatial inaccuracies due to orbit estimation.*



## 📊 Important Parameters in MODIS Data

| Column Name | Description |
|-------------|-------------|
| `latitude` | Center of the 1 km fire pixel (Y-axis) |
| `longitude` | Center of the 1 km fire pixel (X-axis) |
| `bright_t31` | Brightness temp. from Band 31 (Kelvin) |
| `bright_t14` | Brightness temp. from Band 21/22 |
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

### ✅ Prerequisites

- Python 3.8 or above  
- Jupyter Notebook or any IDE  

### 📦 Required Libraries

Install required packages using pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn geopandas jupyter

```


## ✍️ Contributing

Feel free to **fork** this repository, **open issues**, or **submit pull requests** if you wish to contribute to the:

- Model improvement
- Data preprocessing
- Visualization enhancements



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.



## 🙋‍♂️ Acknowledgments

- **NASA FIRMS** for providing open access to MODIS fire data  
- **AICTE** for offering this opportunity under **Internship Cycle 2**



## 📌 Notes

- For installation, use the dependencies listed in `requirements.txt`
- All data used in this project is publicly available

