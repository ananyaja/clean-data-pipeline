import pandas as pd
import numpy as np
import os

def generate_sample_data():
    os.makedirs("data", exist_ok=True)
    
    data = {
        "transaction_id": [1001, 1002, 1003, 1001, 1004, 1005, np.nan, 1006],
        "customer_name": ["  Alice Smith", "Bob Jones ", "Charlie Brown", "  Alice Smith  ", "Diana Prince", "Ethan Hunt", "Fiona Glenanne", "  George Clark"],
        "signup_date": ["2026-01-15", "15/01/2026", "2026-01-18", "2026-01-15", "InvalidDate", "2026-01-20", "2026-01-21", "2026/01/22"],
        "purchase_amount": ["$150.00", " 200.5 ", "$310.25", "$150.00", "N/A", "450.00", "125.75", " $99.99 "],
        "status": ["Completed", "Pending", "Completed", "Completed", "Failed", "Completed", "Pending", "Completed"]
    }
    
    df = pd.DataFrame(data)
    file_path = "data/raw_messy_data.csv"
    df.to_csv(file_path, index=False)
    print(f"[+] Realistic messy sample dataset generated successfully at: {file_path}")

if __name__ == "__main__":
    generate_sample_data()
