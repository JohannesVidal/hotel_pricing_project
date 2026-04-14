
## Data Pipeline

The workflow implemented in this project follows these steps:

1. **City extraction**
   - Query API to retrieve city metadata
   - Extract IATA city codes (e.g., PAR, ROM)

2. **Hotel retrieval**
   - Fetch hotel data per city using city codes

3. **Data normalization**
   - Convert JSON responses into tabular format (DataFrames)

4. **Data merging**
   - Combine datasets from multiple cities

5. **Data cleaning**
   - Rename columns (snake_case)
   - Fix data types (numeric, datetime, boolean)
   - Standardize text fields
   - Remove duplicates

6. **Data validation**
   - Check missing values
   - Ensure uniqueness of hotel IDs

7. **Data storage**
   - Save raw and processed datasets

## Outputs

- **Raw dataset**  
  `data/raw/hotels_paris_rome_raw.csv`

- **Processed base dataset**  
  `data/processed/hotels_paris_rome_base_clean.csv`

This dataset is intended to be used in subsequent analysis projects.

## Future Integration

This dataset will be enriched and combined with:

- Event data (Ticketmaster API)
- Weather data (OpenWeather API)
- Potential pricing / offer data

The final goal is to analyze:

- Demand patterns
- External factors affecting hotel pricing
- Market behavior across cities

## Security

- API keys are stored in a `.env` file and not tracked by Git
- Sensitive information is not included in the repository
- Notebook outputs should be cleared before committing

## Notes

- API rate limits may apply (especially on free tiers)
- Data completeness depends on API availability

---

## Author

Johannes Vidal