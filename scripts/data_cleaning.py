
import pandas as pd

# STEP 1: Read CSV file
df = pd.read_csv("data/sample_orders_150_rows.csv")

print("\n--- ORIGINAL DATA ---")
print(df.head())

# STEP 2: Dataset information
print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- DATASET INFO ---")
df.info()

# STEP 3: Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# STEP 4: Check duplicates
print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# STEP 5: Create a copy
clean_df = df.copy()

# STEP 6: Remove duplicates
clean_df = clean_df.drop_duplicates()

# STEP 7: Handle missing text values
clean_df["CustomerName"] = clean_df["CustomerName"].fillna("Unknown")
clean_df["Product"] = clean_df["Product"].fillna("Unknown")
clean_df["Category"] = clean_df["Category"].fillna("Unknown")
clean_df["Shipped"] = clean_df["Shipped"].fillna("Pending")
clean_df["Country"] = clean_df["Country"].fillna("Unknown")

# STEP 8: Handle missing numeric values
clean_df["Quantity"] = clean_df["Quantity"].fillna(
    clean_df["Quantity"].median()
)

clean_df["Price"] = clean_df["Price"].fillna(
    clean_df["Price"].median()
)

# STEP 9: Validate quantity
print("\n--- INVALID QUANTITY ---")
print(clean_df[clean_df["Quantity"] <= 0])

# STEP 10: Validate price
print("\n--- INVALID PRICE ---")
print(clean_df[clean_df["Price"] <= 0])

# STEP 11: Check final missing values
print("\n--- FINAL MISSING VALUES ---")
print(clean_df.isnull().sum())

# STEP 12: Check duplicates again
print("\n--- FINAL DUPLICATES ---")
print(clean_df.duplicated().sum())

# STEP 13: Create a new column
clean_df["TotalAmount"] = (
    clean_df["Quantity"] * clean_df["Price"]
)

# STEP 14: Display cleaned data
print("\n--- CLEANED DATA ---")
print(clean_df.head())

print("\n--- FINAL SHAPE ---")
print(clean_df.shape)

# STEP 15: Export cleaned dataset
clean_df.to_csv(
    "data/cleaned_orders.csv",
    index=False
)

print("\nCleaned dataset exported successfully!")
