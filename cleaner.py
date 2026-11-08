import pandas as pd
import numpy as np
from datetime import datetime

def load_and_clean_data(file_path):
    print(f"[*] Loading raw dataset from: {file_path}")
    df = pd.read_csv(file_path)
    
    initial_rows = len(df)
    print(f"[*] Initial row count: {initial_rows}")

    # 1. Strip whitespace from all string columns
    str_cols = df.select_dtypes(include=['object']).columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    # 2. Drop absolute duplicate rows
    df = df.drop_duplicates()
    print(f"[*] Dropped {initial_rows - len(df)} duplicate rows.")

    # 3. Handle missing values strategically
    # If customer ID or transaction ID is missing, drop those rows (unrecoverable)
    if 'transaction_id' in df.columns:
        df = df.dropna(subset=['transaction_id'])

    # Fill missing numeric columns with median, text with 'Unknown'
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    for col in str_cols:
        if col != 'transaction_id':
            df[col] = df[col].fillna('Unknown')

    # 4. Standardize date formats (e.g., convert mixed strings to standard datetime)
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # 5. Clean currency or numeric symbols if present (e.g., '$', ',')
    currency_cols = [col for col in df.columns if any(term in col.lower() for term in ['price', 'amount', 'cost', 'revenue'])]
    for col in currency_cols:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace(r'[$,]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')

    print(f"[*] Data cleaning complete. Final clean row count: {len(df)}")
    return df

if __name__ == "__main__":
    # Example execution pipeline
    # raw_df = load_and_clean_data("data/raw_messy_data.csv")
    # raw_df.to_csv("data/clean_output_data.csv", index=False)
    pass
