# Automated ETL Pipeline (CSV → SQLite) using Python

## Overview
This project demonstrates an end-to-end ETL pipeline:
- Extracts retail sales data from a CSV file
- Cleans and transforms data using Pandas
- Loads the output into a SQLite database table
- Validates row counts after loading

## Files
- `Superstore.csv` → input dataset
- `etl_pipeline.py` → ETL script (Extract → Transform → Load)
- `sales.db` → SQLite database created after running the script

## How to Run
```bash
pip install pandas
python etl_pipeline.py
