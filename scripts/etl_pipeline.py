"""
etl_pipeline.py
===============
Airline Reviews Analytics — ETL Pipeline
Newton School of Technology | Capstone 2

Usage:
    python scripts/etl_pipeline.py

Output:
    data/processed/cleaned_airline_reviews.csv
    data/processed/final_airline_reviews.csv
"""

import os
import sys
import logging
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s"
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_FILE = os.path.join(BASE_DIR, "data", "raw", "airline_reviews.csv")
CLEANED_FILE = os.path.join(BASE_DIR, "data", "processed", "cleaned_airline_reviews.csv")
FINAL_FILE = os.path.join(BASE_DIR, "data", "processed", "final_airline_reviews.csv")

# ===========================================================================
# STEP 1 — EXTRACT
# ===========================================================================
def extract(filepath):
    log.info("=== STEP 1: EXTRACT ===")

    if not os.path.exists(filepath):
        log.error(f"File not found: {filepath}")
        sys.exit(1)

    df = pd.read_csv(filepath)

    log.info(f"Shape: {df.shape}")
    log.info(f"Columns: {list(df.columns)}")
    log.info(f"Missing Values:\n{df.isnull().sum()}")

    return df


# ===========================================================================
# STEP 2 — TRANSFORM / CLEAN
# ===========================================================================
def transform(df):
    log.info("=== STEP 2: CLEANING ===")

    # ----------------------------
    # 2.1 Drop useless column
    # ----------------------------
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # ----------------------------
    # 2.2 Standardize columns
    # ----------------------------
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    # ----------------------------
    # 2.3 Handle missing values
    # ----------------------------

    # Drop high-missing columns
    drop_cols = ['wifi_&_connectivity', 'aircraft']
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')

    # Fill categorical
    cat_cols = ['type_of_traveller', 'seat_type', 'route']
    for col in cat_cols:
        if col in df.columns:
            df[col].fillna('Unknown', inplace=True)

    # Fill numerical ratings
    rating_cols = [
        'seat_comfort', 'cabin_staff_service',
        'food_&_beverages', 'ground_service',
        'inflight_entertainment', 'value_for_money'
    ]

    for col in rating_cols:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    # ----------------------------
    # 2.4 Data types
    # ----------------------------
    df['overall_rating'] = pd.to_numeric(df['overall_rating'], errors='coerce')

    if 'review_date' in df.columns:
        df['review_date'] = pd.to_datetime(df['review_date'], errors='coerce')

    if 'date_flown' in df.columns:
        df['date_flown'] = pd.to_datetime(df['date_flown'], errors='coerce')

    # ----------------------------
    # 2.5 Feature engineering
    # ----------------------------
    df['recommended'] = df['recommended'].astype(str).str.lower().str.strip()

    df['is_recommended'] = df['recommended'].map({
        'yes': 1,
        'no': 0
    })

    # ----------------------------
    # 2.6 Drop missing target
    # ----------------------------
    df = df.dropna(subset=['overall_rating'])

    log.info(f"Cleaned shape: {df.shape}")

    return df


# ===========================================================================
# STEP 3 — DERIVED FEATURES (TABLEAU READY)
# ===========================================================================
def create_final_dataset(df):
    log.info("=== STEP 3: FINAL DATA PREP ===")

    # Rating category
    def rating_category(x):
        if x <= 3:
            return 'Low'
        elif x <= 6:
            return 'Medium'
        else:
            return 'High'

    df['rating_category'] = df['overall_rating'].apply(rating_category)

    # Final columns (OPTIMIZED DATASET)
    final_df = df[[
        'airline_name',
        'overall_rating',
        'review_date',
        'seat_type',
        'type_of_traveller',
        'is_recommended',
        'verified',
        'seat_comfort',
        'cabin_staff_service',
        'food_&_beverages',
        'ground_service',
        'inflight_entertainment',
        'value_for_money',
        'rating_category'
    ]]

    return final_df


# ===========================================================================
# STEP 4 — LOAD
# ===========================================================================
def load(df, final_df):
    log.info("=== STEP 4: LOAD ===")

    os.makedirs(os.path.dirname(CLEANED_FILE), exist_ok=True)

    df.to_csv(CLEANED_FILE, index=False)
    final_df.to_csv(FINAL_FILE, index=False)

    log.info(f"Saved cleaned dataset → {CLEANED_FILE}")
    log.info(f"Saved final dataset → {FINAL_FILE}")


# ===========================================================================
# PIPELINE RUNNER
# ===========================================================================
def run_pipeline():
    log.info("🚀 Starting Airline ETL Pipeline")

    df = extract(RAW_FILE)
    df = transform(df)
    final_df = create_final_dataset(df)
    load(df, final_df)

    log.info("✅ Pipeline completed successfully")


# ===========================================================================
# ENTRY POINT
# ===========================================================================
if __name__ == "__main__":
    run_pipeline()
