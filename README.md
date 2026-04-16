# Airbnb Pricing & Tourism Density Analysis (Paris)

## Overview

This project analyzes how **location and tourism intensity influence Airbnb pricing and guest satisfaction in Paris**.

The analysis combines:
- Airbnb listing data
- Hotel data (RapidAPI)
- External geospatial data from the **Geoapify Places API**

The goal is to move beyond simple location assumptions and evaluate whether:
- proximity to landmarks matters
- broader **tourism density** provides a stronger signal for pricing

The full analysis is developed in a Jupyter Notebook, where data is extracted, enriched, and analyzed step by step.

---

## Business Focus

The project is built around two core questions:

### 1. What drives guest satisfaction?
- Does location (proximity to landmarks) matter?
- Or do internal factors such as cleanliness dominate?

### 2. What drives pricing?
- Does tourism density influence Airbnb prices?
- Do highly touristic areas command a price premium?

---

## Key Insight

- **Location (landmark proximity)** -> very weak relationship with satisfaction
- **Cleanliness** -> strong driver of satisfaction
- **Tourism density** -> moderate but consistent relationship with pricing

This leads to a clear distinction:

> Quality drives experience, while location drives price.

---

## Tech Stack

- Python (Pandas, NumPy, Matplotlib)
- APIs:
  - Google Hotel Data (RapidAPI)
  - Geoapify Places API
- Jupyter Notebook
- Git & GitHub

---

## Project Structure

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
    │   ├── geoapify_api.py
    │   ├── ticketmaster_api.py
    │   └── weather_api.py
    │
    ├── .gitignore
    ├── requirements.txt
    └── README.md

---

## Data Pipeline

The project follows a structured workflow:

### 1. Hotel Data Extraction (RapidAPI)
- Retrieve city and hotel data
- Normalize JSON responses into DataFrames
- Clean and standardize fields

### 2. Airbnb Data Preparation
- Clean and structure Airbnb dataset
- Engineer pricing and satisfaction variables

### 3. Location Feature Engineering
- Compute:
  - distance to key landmarks
  - number of nearby points of interest

### 4. Geoapify Enrichment
- Group listings into geographic zones (rounded coordinates)
- Query Geoapify API for nearby tourism POIs
- Create tourism density features:
  - number of POIs
  - attractions / sights / heritage
  - composite density score

### 5. Analysis
- Correlation analysis (pricing and satisfaction)
- Segmentation (density bands)
- Visualization (scatter plots, comparisons)

### 6. Hotel Extension
- Apply tourism density features to hotel locations
- Rank hotels based on exposure to tourism demand

---

## Outputs

Processed datasets generated:

- `airbnb_paris_geoapify_enriched.csv`
- `geoapify_paris_density_features.csv`
- `hotel_paris_geoapify_ranking.csv`

These datasets combine internal and external data into a unified analytical layer.

---

## How to Run the Project

### 1. Clone repository

    git clone https://github.com/JohannesVidal/hotel_pricing_project.git
    cd hotel_pricing_project

### 2. Create environment

    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file in the root directory with your own API keys:

    RAPIDAPI_KEY=your_rapidapi_key_here
    GOOGLE_HOTEL_RAPIDAPI_HOST=google-hotel-data-scaper.p.rapidapi.com
    GEOAPIFY_API_KEY=your_geoapify_key_here
    OPENWEATHER_API_KEY=your_openweather_key_here
    TICKETMASTER_API_KEY=your_ticketmaster_key_here

---

## API Setup

### RapidAPI - Hotel Data

1. Create an account on RapidAPI
2. Subscribe to the Google Hotel Data Scraper API
3. Copy your `x-rapidapi-key`
4. Add it to your `.env` file as `RAPIDAPI_KEY`

This key is required to retrieve hotel data.

### Geoapify - Tourism Data

1. Create an account on Geoapify
2. Generate an API key
3. Add it to your `.env` file as `GEOAPIFY_API_KEY`

This API is used to extract **points of interest around each location**, which are then transformed into tourism density features.

### Optional APIs

- OpenWeather -> weather enrichment
- Ticketmaster -> events enrichment

These are not required for the core analysis.

---

## Important Notes

- The Geoapify API is limited (max 20 POIs per request)
- Tourism variables should be interpreted as:

  > proxies for tourism intensity, not exact counts

- API rate limits may affect reproducibility if rerunning the notebook
- Due to API limitations, the final analysis is focused on **Paris only**

---

## Limitations

- Pricing is influenced by many factors not included in the dataset:
  - property type
  - amenities
  - host behavior
- Tourism density is an approximation due to API constraints
- The project is designed as an analytical case study, not as a production data pipeline

---

## Project Context

This repository focuses on:
- data extraction
- feature engineering
- analytical validation

The main value lies in combining:
- internal listing data
- external geospatial signals

to build a more realistic view of **urban pricing dynamics**.

The notebook contains the full step-by-step analysis, so this README is intentionally kept concise.

---

## Author

Johannes Vidal
