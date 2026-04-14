# 🏨 Hotel Data Pipeline for Market Analysis

## 📌 Overview

This project is part of a broader data analysis focused on **Airbnb and hotel market behavior**.

The main objective is to support business-driven questions such as:

- Does the day of the week affect cleanliness ratings and guest satisfaction on Airbnb?
- Does being a superhost impact pricing and guest satisfaction?
- How does location influence pricing and ratings across Airbnb and hotels?

To support this analysis, this repository builds a **data pipeline that extracts and prepares hotel data**, which will later be combined with external datasets.

This pipeline acts as a **data enrichment layer**, enabling:

- Geographic analysis (e.g., heatmaps of listing distribution)
- Cross-platform comparisons (Airbnb vs hotels)
- Integration with external signals (events, weather)

---

## ❓ Business Questions

This project contributes to answering the following hypotheses:

### 1. Weekday vs Weekend Impact
**Question:**  
Does the day of the week affect cleanliness ratings and overall guest satisfaction on Airbnb?

**Hypothesis:**  
Listings will have lower cleanliness ratings and guest satisfaction scores on weekends due to higher turnover and reduced cleaning time.

---

### 2. Superhost Effect
**Question:**  
Does being a superhost impact pricing and guest satisfaction?

**Hypothesis:**  
Superhost listings will show:
- Higher guest satisfaction scores
- Better cleanliness ratings
- Higher average price per night

---

### 3. Location & Market Structure
**Question:**  
Are hotel and Airbnb listings concentrated in specific neighbourhoods, and does location affect pricing or ratings?

**Hypothesis:**  
Listings closer to city centres and major attractions will have higher prices, but not necessarily higher satisfaction scores.

---

## ⚙️ Tech Stack

- **Python** (Pandas, Requests)
- **APIs**
  - Google Hotel Data (RapidAPI)
  - Ticketmaster (optional)
  - OpenWeather (optional)
- **Jupyter Notebook**
- **Git & GitHub**

---

## 🧠 Project Structure

```text
hotel_pricing_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_hotel_data_extraction.ipynb
│
├── src/
│   ├── config.py
│   ├── ticketmaster_api.py
│   └── weather_api.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔄 Data Pipeline

The workflow implemented in this project follows these steps:

### 1. City Extraction
- Query API to retrieve city metadata
- Extract IATA city codes (e.g., `PAR`, `ROM`)

### 2. Hotel Retrieval
- Fetch hotel data per city using city codes

### 3. Data Normalization
- Convert JSON responses into tabular format (DataFrames)

### 4. Data Merging
- Combine datasets from multiple cities

### 5. Data Cleaning
- Rename columns (`snake_case`)
- Fix data types (numeric, datetime, boolean)
- Standardize text fields
- Remove duplicates

### 6. Data Validation
- Check missing values
- Ensure uniqueness of hotel IDs

### 7. Data Storage
- Save raw and processed datasets

---

## 📊 Outputs

### Raw dataset
`data/raw/hotels_paris_rome_raw.csv`

### Processed dataset
`data/processed/hotels_paris_rome_base_clean.csv`

This dataset serves as a **base layer for further analysis and enrichment**.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/JohannesVidal/hotel_pricing_project.git
cd hotel_pricing_project
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```text
.env
```

Add the following:

```env
RAPIDAPI_KEY=your_rapidapi_key_here
GOOGLE_HOTEL_RAPIDAPI_HOST=google-hotel-data-scaper.p.rapidapi.com

OPENWEATHER_API_KEY=your_openweather_key_here
TICKETMASTER_API_KEY=your_ticketmaster_key_here
```

---

## 🔑 API Setup

To run this project, you need API keys from the following providers:

### RapidAPI (Hotel Data)
1. Create an account on RapidAPI
2. Subscribe to the Google Hotel Data Scraper API
3. Copy your `x-rapidapi-key`

### OpenWeather (optional)
1. Create an account
2. Generate an API key

### Ticketmaster (optional)
1. Create a developer account
2. Generate an API key

---

## 🔗 Data Enrichment Roadmap

- Integrate hotel data with Airbnb datasets
- Build geospatial analysis (heatmaps, clustering)
- Enrich dataset with:
  - Event data (Ticketmaster API)
  - Weather data (OpenWeather API)
- Enable cross-platform comparison (Airbnb vs hotels)

---

## ⚠️ Limitations

- API rate limits apply (especially free tiers)
- Data completeness depends on API availability
- Some endpoints may return limited results depending on quota

---

## 🔒 Security

- `.env` file is not tracked by Git
- API keys are never exposed
- Sensitive information is excluded from the repository

---

## 🎯 Project Context

This repository focuses on **data extraction and preparation**.

The full analytical workflow includes:
- External datasets (Airbnb data)
- Exploratory data analysis
- Visualization (e.g., Power BI dashboards)

---

## 👤 Author

**Johannes Vidal**
