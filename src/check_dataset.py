from pathlib import Path
import pandas as pd

# Run from any directory: python src/check_dataset.py
project_root = Path(__file__).resolve().parents[1]
csv_path = project_root / "data" / "raw" / "superstore_sales.csv"
df = pd.read_csv(csv_path, dtype={"Postal Code": "string"})

print("DATASET INSPECTION")
print("Rows, columns:", df.shape)
print("Columns:", df.columns.tolist())
print("First 5 rows:\n", df.head().to_string(index=False))
print("Missing values:\n", df.isna().sum().to_string())
print("Exact duplicate rows across entire mixed CSV:", df.duplicated().sum())

is_order = pd.to_numeric(df["Row ID"], errors="coerce").notna()
orders = df.loc[is_order].copy()
print("\nActual sales-line rows:", len(orders))
print("Non-sales People/Returns rows:", len(df) - len(orders))
print("Exact duplicates within sales rows:", orders.duplicated().sum())
print("Missing postcodes in sales rows:", orders["Postal Code"].isna().sum())
